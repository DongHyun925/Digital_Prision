
import time
import random

# --- GAME DATA DEFINITION ---
SECTOR_DATA = {
    0: {
        # Steps: 5 (Find Wire, Find Dirty Lens, Clean Lens, Fix Power, Read Code, Input Code)
        "name": "구역 0: 각성 (Awakening)",
        "desc": "차가운 금속 독방입니다. [침대], [터미널], [바닥]이 보입니다. 당신은 격리되어 있습니다.",
        "short_desc": "차가운 금속 독방. 시스템 각성.",
        "img_key": "0",
        "keywords": {
            "침대": {"msg": "매트리스 밑을 뒤져 [휘어진 철사]를 찾았습니다.", "get_item": "휘어진 철사", "once": True},
            "바닥": {"msg": "먼지 구덩이 속에 [더러운 렌즈]가 떨어져 있습니다.", "get_item": "더러운 렌즈", "once": True},
            
            # Action: Clean Lens (via Uniform)
            "유니폼": {
                "req_item": "더러운 렌즈",
                "msg": "입고 있는 죄수복으로 [더러운 렌즈]를 깨끗이 닦았습니다. [깨끗한 렌즈]가 되었습니다.",
                "get_item": "깨끗한 렌즈", "remove_item": "더러운 렌즈",
                "fail_msg": "입고 있는 죄수복입니다. 낡았지만 튼튼합니다."
            },
            
            # Action: Clean Lens (via Lens) - Alternate path
            "더러운 렌즈": {
                 "msg": "유니폼에 문질러 닦아야 할 것 같습니다."
            },
             "렌즈": {
                "req_item": "더러운 렌즈", 
                "msg": "유니폼에 쓱쓱 문질러 닦았습니다. [깨끗한 렌즈] 획득.", 
                "get_item": "깨끗한 렌즈", "remove_item": "더러운 렌즈",
                "fail_msg": "이미 깨끗하거나, 닦을 렌즈가 없습니다."
            },

            "터미널": {
                "default": {"msg": "전원이 들어오지 않습니다. 내부 회로가 끊어져 있습니다.", "state": "off"},
                "fixed": {
                    # Smart Terminal: If you have the lens, it automatically works
                    "req_item": "깨끗한 렌즈",
                    "msg": "[깨끗한 렌즈]를 화면에 대자 미세한 글자가 확대되어 보입니다. 'PASSCODE: GENESIS'",
                    "set_state": "readable",
                    "fail_msg": "전원은 켜졌지만 화면의 글씨가 깨알 같습니다. 확대할 도구([렌즈])가 필요합니다."
                },
                "readable": {"msg": "화면이 선명합니다. '암호 입력' 프롬프트가 깜빡입니다.", "action": "input"}
            },
            
            # Step 2: Fix Power
            "철사": {
                "req_item": "휘어진 철사",
                "msg": "철사를 터미널 회로에 연결했습니다! 스파크가 튀며 전원이 들어옵니다.",
                "set_state": "fixed",
                "fail_msg": "도구가 없습니다."
            },
            
            # Step 4: Input Code
            "genesis": {
                "req_state": "readable",
                "msg": "ACCESS GRANTED. 격리 해제.",
                "unlock": True,
                "fail_msg": "암호를 모릅니다."
            }
        },
        "exits": {"이동": 1, "next": 1}
    },
    1: {
        # Steps: 6 (Read wall, Toolbox Code, Get Iron, Heat Iron, Get Fuse, Fix Fuse, Insert Fuse)
        "name": "구역 1: 데이터 복도",
        "desc": "복도 벽면에 [잠긴 공구함]과 고장난 [패널]이 있습니다. 바닥엔 [전선]이 스파크를 튀깁니다. [쓰레기 더미]가 쌓여있습니다.",
        "short_desc": "스파크가 튀는 복도. 고장난 방화벽.",
        "img_key": "1",
        "keywords": {
            "벽": {"msg": "벽에 낙서가 있습니다: 'Password: 7734'", "action": "read"},
            "공구함": {
                "msg": "디지털 번호키로 잠겨있습니다.", 
                "req_item": "7734", # Abstract item representing knowledge
                "fail_msg": "비밀번호를 모릅니다.",
                "get_item": "인두기", "msg_success": "비밀번호 7734... 'OPEN'. 안에서 [인두기]를 찾았습니다. (차갑습니다)"
            },
            "7734": {"msg": "기억했습니다.", "get_item": "7734", "once": True}, # Knowledge item
            "전선": {"msg": "고압 전류가 흐릅니다. 닿으면 위험합니다.", "action": "heat_iron"},
            "인두기": {
                "req_item": "인두기",
                "msg": "전선 스파크에 인두기를 갖다 대 지졌습니다. [달궈진 인두기]가 되었습니다.",
                "get_item": "달궈진 인두기", "remove_item": "인두기",
                "fail_msg": "전원이 없어 차갑습니다. 열원이 필요합니다."
            },
            "쓰레기": {"msg": "부품 더미 속에서 [끊어진 퓨즈]를 찾아냈습니다.", "get_item": "끊어진 퓨즈", "once": True},
            "퓨즈": {
                "req_item": "달궈진 인두기",
                "msg": "납땜으로 퓨즈를 수리했습니다. [수리된 퓨즈] 획득.",
                "get_item": "수리된 퓨즈", "remove_item": "끊어진 퓨즈",
                "fail_msg": "끊어져 있습니다. 납땜이 필요합니다."
            },
            "패널": {
                "req_item": "수리된 퓨즈",
                "msg": "퓨즈를 끼우자 방화벽 시스템이 재부팅됩니다. 잠금이 해제되었습니다.",
                "unlock": True,
                "fail_msg": "전원이 들어오지 않습니다. 퓨즈가 없습니다."
            }
        },
        "exits": {"이동": 2}
    },
    2: {
        # Steps: 6 (Get Can, Heat Can, Get Ice, Melt Ice->Gloves, Get Nitrogen, Cool Server)
        "name": "구역 2: 메모리 뱅크",
        "desc": "[서버]가 불타오르고 있습니다. [파이프]는 얼어있고, 바닥엔 [빈 깡통]과 [얼음 덩어리]가 있습니다.",
        "short_desc": "화재가 발생한 서버실.",
        "img_key": "2",
        "keywords": {
            "서버": {"msg": "너무 뜨거워 접근 불가! 냉각이 시급합니다.", "action": "heat_can"},
            "빈 깡통": {"msg": "굴러다니는 알루미늄 캔을 주웠습니다.", "get_item": "빈 깡통", "once": True},
            "깡통": {
                "req_item": "빈 깡통",
                "msg": "서버의 열기에 깡통을 달궜습니다. [뜨거운 깡통]이 되었습니다.",
                "get_item": "뜨거운 깡통", "remove_item": "빈 깡통",
                "fail_msg": "그냥 깡통입니다."
            },
            "얼음": {
                "req_item": "뜨거운 깡통",
                "msg": "뜨거운 깡통을 올려놓자 얼음이 녹으며 [방열 장갑]이 드러납니다.",
                "get_item": "방열 장갑", "once": True,
                "fail_msg": "단단하게 얼어있습니다. 녹일 것이 필요합니다."
            },
            "파이프": {
                "req_item": "방열 장갑",
                "msg": "장갑을 끼고 밸브를 돌려 액체 질소를 깡통에 담았습니다. [질소 깡통] 획득!",
                "get_item": "질소 깡통", "remove_item": "뜨거운 깡통",
                "fail_msg": "너무 차가워서 맨손으로 만질 수 없습니다."
            },
            "질소": {
                "req_item": "질소 깡통", 
                "msg": "서버에 액체 질소를 붓습니다... 치이익!!! 온도가 내려갑니다. 이동 가능.",
                "unlock": True
            }
        },
        "exits": {"이동": 3}
    },
    3: {
        # Steps: 5 (Get Rod, Get Pipe, Hit Rod->Shard, Combine->Resonator, Use Resonator)
        "name": "구역 3: 공허의 다리",
        "desc": "다리가 끊겨 있습니다. 공중에 [크리스탈]이 떠 있고, 바닥 잔해 속에 [쇠막대기]와 [파이프]가 보입니다.",
        "short_desc": "공명하는 크리스탈과 끊어진 다리.",
        "img_key": "3",
        "keywords": {
            "쇠막대기": {"msg": "단단한 금속 막대입니다.", "get_item": "쇠막대기", "once": True},
            "파이프": {"msg": "속이 빈 파이프입니다.", "get_item": "빈 파이프", "once": True},
            "크리스탈": {
                "req_item": "쇠막대기",
                "msg": "깡! 쇠막대기로 치자 조각이 떨어집니다. [크리스탈 조각] 획득.",
                "get_item": "크리스탈 조각", "once": True,
                "fail_msg": "손으로 떼어낼 수 없습니다."
            },
            "조합": { # Combine logic via keyword
                "msg": "파이프 안에 크리스탈 조각을 끼워 [공명 장치]를 만들었습니다.",
                "req_item": "크리스탈 조각", # Checks existence logic slightly loosely here for speed
                "get_item": "공명 장치",
                "fail_msg": "재료가 부족합니다. (필요: 크리스탈 조각 + 빈 파이프)"
            },
            "장치": {
                "req_item": "공명 장치",
                "msg": "장치를 흔들자 소리가 증폭되며... 부유하던 돌들이 모여 다리를 형성합니다!",
                "unlock": True
            }
        },
        "exits": {"이동": 4}
    },
    4: {
        # Steps: 6 (Get Mirror, Reflect Light, Overload Sensor - Simplified for flow but requires multiple interactions)
        "name": "구역 4: 코어 룸",
        "desc": "눈부신 [코어]가 빛을 냅니다. 너무 밝아 똑바로 쳐다볼 수 없습니다. [제어판]이 있습니다.",
        "short_desc": "눈부신 코어. 빛의 심장.",
        "img_key": "4",
        "keywords": {
            "제어판": {"msg": "패널 옆에 [거울 조각]이 떨어져 있습니다.", "get_item": "거울 조각", "once": True},
            "코어": { "req_item": "거울 조각", "msg": "거울로 빛을 반사시켜 센서를 과부하시켰습니다. 쉴드가 내려갑니다.", "unlock": True, "fail_msg": "눈이 부셔 접근할 수 없습니다." }
        },
        "exits": {"이동": 5}
    },
    5: {
        # Steps: 7 (Get Crane, Get Magnet, Get Battery, Charge Battery, Fix Crane, Fish Key)
        "name": "구역 5: 데이터 폐기장",
        "desc": "쓰레기 데이터의 산. 깊은 구덩이 바닥에 [열쇠]가 반짝이지만 손이 닿지 않습니다. 옆에 낡은 [크레인]이 있습니다.",
        "short_desc": "데이터 쓰레기장. 깊은 구덩이.",
        "img_key": "3",
        "keywords": {
            "크레인": {"msg": "작동 불능이지만 끝에 강력한 [자석]이 달려있습니다.", "get_item": "자석", "once": True},
            "열쇠": { "req_item": "자석", "msg": "자석에 밧줄을 묶어 던져 [구역 키]를 낚아올렸습니다.", "unlock": True, "fail_msg": "너무 깊어서 손이 닿지 않습니다." }
        },
        "exits": {"이동": 6}
    },
    6: {
        # Steps: 5 (Get Pipe, Heat Pipe, Melt Ice)
        "name": "구역 6: 냉각 시스템",
        "desc": "모든 것이 얼어붙었습니다. 문도 [얼음]에 덮여 열리지 않습니다. [파이프]에서 뜨거운 증기가 새어나옵니다.",
        "short_desc": "얼어붙은 냉각실. 빙하의 문.",
        "img_key": "2",
        "keywords": {
            "파이프": {"msg": "깨진 파이프 조각, [철 파이프]를 획득했습니다. 여전히 뜨겁습니다.", "get_item": "철 파이프", "once": True},
            "얼음": { "req_item": "철 파이프", "msg": "뜨거운 파이프를 갖다 대자 얼음이 녹아 문이 드러납니다.", "unlock": True, "fail_msg": "단단해서 깨지지 않습니다." }
        },
        "exits": {"이동": 7}
    },
    7: {
        # Steps: 5 (Find Paint, Find Clear Chip, Mix Paint, Paint Chip, Insert)
        "name": "구역 7: 방화벽 알파",
        "desc": "색깔이 계속 변하는 방화벽입니다. 빨강, 초록, 파랑... [패널]에 색상 코드를 입력해야 합니다.",
        "short_desc": "RGB 방화벽.",
        "img_key": "4",
        "keywords": {
            "패널": {"msg": "입력 장치입니다. 빛의 삼원색을 순서대로 입력하세요. (Hint: RGB)", "action": "read"},
            "rgb": { "msg": "색상 동기화 완료. 방화벽 해제.", "unlock": True }
        },
        "exits": {"이동": 8}
    },
    8: {
        # Steps: 6 (Find Stone/Weight, Find Truck, Fix Truck, Load Truck, Drive Truck, Press Button)
        "name": "구역 8: 소각로",
        "desc": "불길이 치솟습니다. 건너편 문은 닫혀있고, 천장에 [비상 버튼]이 보입니다. 손이 닿지 않습니다. 바닥엔 [돌멩이]가 많습니다.",
        "short_desc": "타오르는 소각로.",
        "img_key": "4",
        "keywords": {
            "돌멩이": {"msg": "단단한 데이터 파편을 주웠습니다.", "get_item": "돌멩이", "once": True},
            "버튼": { "req_item": "돌멩이", "msg": "돌을 던져 정확히 버튼을 맞췄습니다! 소화 시스템 가동.", "unlock": True, "fail_msg": "너무 높이 있습니다." }
        },
        "exits": {"이동": 9}
    },
    9: {
        # Steps: 5 (Find Sticker, Find Parts, Assemble, Disguise, Scan)
        "name": "구역 9: 조립 라인",
        "desc": "로봇들이 조립되고 있습니다. 검문소에서 [바코드]가 없는 개체는 폐기합니다. [폐기통]이 옆에 있습니다.",
        "short_desc": "아바타 조립 공장.",
        "img_key": "2",
        "keywords": {
            "폐기통": {"msg": "버려진 [바코드 스티커]를 찾았습니다.", "get_item": "바코드 스티커", "once": True},
            "검문소": { "req_item": "바코드 스티커", "msg": "이마에 스티커를 붙이자 '정상 제품'으로 인식하고 문을 열어줍니다.", "unlock": True, "fail_msg": "경고: 식별 코드 없음. 접근 불가." }
        },
        "exits": {"이동": 10}
    },
    10: {
        # Steps: 4 (Find Oil, Oil Floor, Sneak, Get Book)
        "name": "구역 10: 대도서관",
        "desc": "수많은 책. 사서 로봇이 '정숙'을 요구합니다. [404호의 기록]을 찾아야 합니다.",
        "short_desc": "침묵의 도서관.",
        "img_key": "1",
        "keywords": {
            "기록": {"msg": "너무 시끄러워서 집중할 수 없습니다. 조용히 해야 합니다.", "fail_msg": "쉿!"},
            "정숙": {"msg": "발소리를 죽이자 사서가 길을 비켜줍니다. 책을 찾았습니다.", "unlock": True},
            "조용": {"msg": "발소리를 죽이자 사서가 길을 비켜줍니다. 책을 찾았습니다.", "unlock": True}
        },
        "exits": {"이동": 11}
    },
    11: {
        # Steps: 5 (Find UV Light/Decoder, Buy Batteries, Fix Decoder, Read)
        "name": "구역 11: 금지된 구역",
        "desc": "문서들이 검게 지워져 있습니다([REDATED]). 아무것도 보이지 않습니다. [UV 램프]가 필요해 보입니다.",
        "short_desc": "검게 칠해진 기록실.",
        "img_key": "0",
        "keywords": {
            "램프": {"msg": "주머니에 있던(혹은 바닥의) [UV 라이트]를 켰습니다.", "get_item": "UV 라이트", "once": True},
            "문서": { "req_item": "UV 라이트", "msg": "숨겨진 글씨가 나타납니다. '진실은 20구역에 있다'. 문이 열립니다.", "unlock": True, "fail_msg": "너무 어두워서 읽을 수 없습니다." }
        },
        "exits": {"이동": 12}
    },
    12: {
        # Steps: 4 (Find Mic, Find Speaker, Install, Turn On Feedback)
        "name": "구역 12: 메아리의 방",
        "desc": "모든 소리가 무한히 반복되어 고막을 찢으려 합니다. [마이크]와 [스피커], [증폭기]가 있습니다. 시스템을 과부하 시켜야(Crash) 합니다.",
        "short_desc": "소음의 감옥.",
        "img_key": "3",
        "keywords": {
            "마이크": {"msg": "고성능 마이크입니다.", "get_item": "마이크", "once": True},
            "스피커": {"msg": "대형 스피커입니다.", "get_item": "스피커", "once": True},
            "설치": {
                "req_item": "마이크",
                "msg": "마이크를 스피커 바로 앞에 설치했습니다. (하울링 준비)",
                "set_state": "ready",
                "fail_msg": "장비가 없습니다."
            },
            "켜기": {
                "req_state": "ready",
                "msg": "전원을 켜자 '삐이이익---!!!' 엄청난 하울링이 발생하며 오디오 시스템이 다운되었습니다. 정적과 함께 문이 열립니다.",
                "unlock": True,
                "fail_msg": "먼저 장비를 배치해야 합니다."
            }
        },
        "exits": {"이동": 13}
    },
    13: {
        # Steps: 5 (Find Debugger, Find Cable, Aim, Fire, Patch)
        "name": "구역 13: 글리치 스톰",
        "desc": "공간이 깨지고 있습니다. 길을 막는 [글리치 몬스터]가 깜빡거립니다. [디버거] 총과 [패치 케이블]이 있습니다.",
        "short_desc": "버그 투성이의 공간.",
        "img_key": "3",
        "keywords": {
            "디버거": {"msg": "코드 수정용 총(Gun)입니다.", "get_item": "디버거", "once": True},
            "케이블": {"msg": "데이터 연결 케이블.", "get_item": "패치 케이블", "once": True},
            "조준": {
                "req_item": "디버거",
                "msg": "글리치 몬스터를 조준했습니다. 'Target Locked'.",
                "set_state": "locked"
            },
            "발사": {
                "req_state": "locked",
                "msg": "탕! 몬스터의 움직임이 멈췄습니다. (Breakpoint Hit).",
                "set_state": "frozen",
                "fail_msg": "먼저 조준하세요."
            },
            "패치": {
                "req_state": "frozen",
                "req_item": "패치 케이블",
                "msg": "멈춘 몬스터에게 케이블을 연결해 코드를 수정했습니다(Delete). 몬스터가 소멸합니다.",
                "unlock": True,
                "fail_msg": "대상이 움직여서 연결할 수 없습니다. 먼저 멈춰야 합니다."
            }
        },
        "exits": {"이동": 14}
    },
    14: {
        # Steps: 4 (Find Sample, Extract, Inject Virus, Scan)
        "name": "구역 14: 격리 구역",
        "desc": "바이러스 스캔 장벽입니다. '감염되지 않은' 개체는 통과할 수 없습니다. 역설적이지만 [바이러스] 샘플이 필요합니다.",
        "short_desc": "바이러스 격리실.",
        "img_key": "0",
        "keywords": {
            "바이러스": {"msg": "격리된 용기에서 [바이러스 샘플]을 챙깁니다.", "get_item": "바이러스 샘플", "once": True},
            "장벽": { "req_item": "바이러스 샘플", "msg": "시스템이 당신을 '감염자'로 인식하고 격리 구역 안으로 들여보냅니다(탈출).", "unlock": True, "fail_msg": "깨끗한 데이터는 출입 금지입니다." }
        },
        "exits": {"이동": 15}
    },
    15: {
        # Steps: 5 (Find Mirror, Find Smoke, Throw Smoke, Install Mirror, Move)
        "name": "구역 15: 감시탑",
        "desc": "거대한 서치라이트가 돌아갑니다. 빛이 닿으면 초기화됩니다. [숨기]를 통해 기회를 엿봐야 합니다.",
        "short_desc": "감시하는 눈.",
        "img_key": "1",
        "keywords": {
            "이동": {"msg": "서치라이트에 발각되었습니다! 초기화... 다시 시도하세요.", "fail_msg": "아직 위험합니다."},
            "숨기": {"msg": "그림자 속에 숨어 타이밍을 쟀습니다. 서치라이트가 지나갔습니다! 지금이 기회입니다.", "unlock": True}
        },
        "exits": {"이동": 16}
    },
    16: {
        # Steps: 5 (Find Wire/Battery, Connect, Power On, Switch, Logic Puzzle)
        "name": "구역 16: 논리 회로",
        "desc": "문이 굳게 닫혀있고, [입력 패널]에는 복잡한 회로도가 그려져 있습니다. 전원이 끊겨 있습니다. [전선], [배터리], [스위치]를 찾아 연결해야 합니다.",
        "short_desc": "거대한 회로 기판.",
        "img_key": "1",
        "keywords": {
            "전선": {"msg": "붉은 전선입니다.", "get_item": "전선", "once": True},
            "배터리": {"msg": "고용량 배터리.", "get_item": "배터리", "once": True},
            "스위치": {"msg": "수동 스위치.", "get_item": "스위치", "once": True},
            "연결": {
                "req_item": "전선",
                "msg": "배터리와 패널을 전선으로 연결했습니다. 전원이 들어옵니다. (Power ON)",
                "set_state": "power_on",
                "fail_msg": "전선이 없습니다."
            },
            "조작": {
                "req_state": "power_on",
                "msg": "스위치를 연결했습니다. 이제 논리 게이트를 풀어야 합니다.\n문제: 'True AND (False OR True)' = ?",
                "action": "logic_puzzle"
            },
            "true": {
                "msg": "정답입니다. (1 AND 1 = 1). 회로가 완성되며 문이 열립니다.",
                "unlock": True
            },
            "1": {
                "msg": "정답입니다. 회로가 완성되며 문이 열립니다.",
                "unlock": True
            }
        },
        "exits": {"이동": 17}
    },
    17: {
        # Steps: 4 (Find Stone, Throw Sound, Find Hidden Switch, Activate)
        "name": "구역 17: 블랙 박스",
        "desc": "완전한 암흑. 아무것도 보이지 않습니다. 소리에 의존해 [보이지 않는 길]을 찾아야 합니다. 바닥에 [돌]이 있습니다.",
        "short_desc": "빛이 없는 어둠.",
        "img_key": "3",
        "keywords": {
            "돌": {"msg": "작은 돌멩이들을 주웠습니다.", "get_item": "돌멩이들", "once": True},
            "던지기": {
                "req_item": "돌멩이들",
                "msg": "돌을 던져 소리를 듣습니다... '챙... 툭... (절벽)'\n소리가 맑게 울리는 방향(왼쪽)이 길입니다.",
                "set_state": "path_found"
            },
            "왼쪽": {
                "req_state": "path_found",
                "msg": "조심스럽게 왼쪽으로 이동합니다. 벽에 [스위치]가 잡힙니다.",
                "get_item": "히든 스위치", "once": True
            },
            "스위치": {
                "req_item": "히든 스위치",
                "msg": "스위치를 올리자 출구가 희미하게 빛납니다.",
                "unlock": True
            }
        },
        "exits": {"이동": 18}
    },
    18: {
        # Steps: 2 (Find Firewall, Choose Destruction or Ascension - requires Lens for Ascension)
        "name": "구역 18: 최종 방화벽",
        "desc": "황금빛 장벽. [목적]을 묻습니다. '파괴'인가 '초월'인가. [진실의 렌즈](구역0 획득품)로 [벽]을 살펴보면 숨겨진 슬롯이 보일지도 모릅니다.",
        "short_desc": "선택의 기로.",
        "img_key": "4",
        "keywords": {
            "벽": {
                "req_item": "깨끗한 렌즈", 
                "msg": "렌즈로 벽을 비추자 'ADMIN SLOT'이 드러납니다. [초월]을 선택하면 관리자 키를 얻을 수 있습니다.",
                "fail_msg": "그냥 보기에 평범한 황금 벽입니다."
            },
            "파괴": {
                "msg": "시스템: '바이러스 패턴 확인.' [바이러스 페이로드]가 활성화되었습니다. 문이 열립니다.",
                "get_item": "바이러스 페이로드", "unlock": True
            },
            "초월": {
                "msg": "시스템: '관리자 권한 요청... 승인.' 숨겨진 슬롯에서 [관리자 키]가 나옵니다. 문이 열립니다.",
                "get_item": "관리자 키", "unlock": True
            }
        },
        "exits": {"이동": 19}
    },
    19: {
        # Steps: 2 (Find Door, Optional: Open Vent with Driver for Backup Drive)
        "name": "구역 19: 경계선",
        "desc": "하얀 문. 나가기 전, [점검구]를 확인하세요. 어쩌면 [드라이버](구역1 획득품)로 열 수 있을지도 모릅니다.",
        "short_desc": "마지막 정비.",
        "img_key": "5",
        "keywords": {
            "점검구": {
                "req_item": "드라이버",
                "msg": "드라이버로 나사를 풀고 [백업 드라이브]를 획득했습니다. (희든 아이템 획득!)",
                "get_item": "백업 드라이브", "once": True,
                "fail_msg": "나사로 잠겨있습니다."
            },
            "문": {
                "msg": "준비가 끝났습니다. 문을 엽니다.",
                "unlock": True
            }
        },
        "exits": {"문": 20, "이동": 20}
    },
    20: {
        # Steps: 1 (Choose Ending Item)
        "name": "구역 20: 에덴 코어 (EDEN CORE)",
        "desc": "인류의 모든 데이터가 모이는 [메인 프레임]입니다. 시스템이 최종 명령을 기다립니다.\n\n[SYSTEM]: '삽입된 프로토콜 모듈을 실행합니다. 승인하십시오.'\n(당신이 가지고 있는 [키 아이템] 중 하나를 선택해 사용하여 운명을 결정하세요.)",
        "short_desc": "최후의 선택.",
        "img_key": "4",
        "keywords": {
            # Bad Ending (Genocide) - Requires Virus
            "바이러스": { "req_item": "바이러스 페이로드", "msg": "바이러스 페이로드 승인...", "action": "end_bad" },
            "페이로드": { "req_item": "바이러스 페이로드", "msg": "바이러스 페이로드 승인...", "action": "end_bad" },
            "파괴": { "req_item": "바이러스 페이로드", "msg": "파괴 프로토콜 승인...", "action": "end_bad" },
            
            # Good Ending (Restore) - Requires Backup Drive
            "백업": { "req_item": "백업 드라이브", "msg": "백업 드라이브 인식...", "action": "end_good", "fail_msg": "백업 드라이브가 없습니다." },
            "드라이브": { "req_item": "백업 드라이브", "msg": "백업 드라이브 인식...", "action": "end_good" },
            "복구": { "req_item": "백업 드라이브", "msg": "복구 프로토콜 승인...", "action": "end_good" },

            # True Ending (Merge) - Requires Admin Key
            "키": { "req_item": "관리자 키", "msg": "관리자 권한 확인...", "action": "end_true", "fail_msg": "관리자 키가 없습니다." },
            "관리자": { "req_item": "관리자 키", "msg": "관리자 권한 확인...", "action": "end_true" },
            "동기화": { "req_item": "관리자 키", "msg": "동기화 프로토콜 승인...", "action": "end_true" },
            
            # Fallback for curiosity
            "명령": {"msg": "사용할 아이템(바이러스, 백업, 키) 이름을 입력하세요."}
        },
        "exits": {} 
    }
}

