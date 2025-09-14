import os


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


# 게임 데이터
# 1. 체력(1-100) 2. 공격력(1-100) 3. 방어력(1-100) 4. 속도(1-5)
jobs = {
    "전사": (70, 60, 60, 3),
    "도적": (35, 90, 20, 5),
    "궁수": (55, 75, 40, 4),
    "방패병": (100, 50, 70, 1)
}

player = {}

# 1. 체력 2. 공격력 3. 방어력 4. 속도(1-10)
environment = {
    "슬라임": (60, 15, 5, 1),
    "고블린": (100, 35, 5, 3),
    "거인": (500, 60, 0, 2),
    "드래곤": (750, 90, 30, 5),
}


# 캐릭터 선택
clear_screen()
print()
print("🎮 캐릭터 목록 🎮")
print()
print("==========================================")
print()
print("1. ⚔️  전사")
print("   스탯: HP:70  ATK:60  DEF:60  SPD:3")
print("   특징: 균형잡힌 올라운더")
print()
print("2. 🗡️  도적")
print("   스탯: HP:35  ATK:90  DEF:20  SPD:5")
print("   특징: 빠르고 강한 암살자")
print()
print("3. 🏹  궁수")
print("   스탯: HP:55  ATK:75  DEF:40  SPD:4")
print("   특징: 안정적인 원거리 딜러")
print()
print("4. 🛡️  방패병")
print("   스탯: HP:100  ATK:50  DEF:90  SPD:1")
print("   특징: 최고의 방어력을 가진 탱커")
print()
print("==========================================")
print("💡 HP=체력, ATK=공격력, DEF=방어력, SPD=공격속도")
print()
print()
print("4 명의 캐릭터중 하나를 골라주세요!")

choice = input("1~4 중 하나를 선택해주세요 (번호입력): ")

if choice == "1":
    print("⚔️ 전사를 선택하셨습니다")
    print("💪 균형잡힌 올라운로 어떤 상황에서도 활약 가능!")
    job = "전사"
elif choice == "2":
    print("🗡️ 도적을 선택하셨습니다")
    print("⚡ 빠르고 강한 암살자로 데미지 플레이가 가능!")
    job = "도적"
elif choice == "3":
    print("🏹 궁수를 선택하셨습니다")
    print("🏹 안정적인 원거리 딜러로 안정적인 플레이가 가능!")
    job = "궁수"
elif choice == "4":
    print("🛡️ 방패병을 선택하셨습니다")
    print("🛡️ 최고의 방어력을 가진 탱커로 언제든지 안전한 플레이가 가능!")
    job = "방패병"
else:
    print("1~4에 있는 숫자만 입력해주세요!")
    exit()

clear_screen()

# 플레이어 정보 설정
hp, attack, defense, speed = jobs[job]
player["job"] = job
player["hp"] = hp
player["max_hp"] = hp
player["attack"] = attack
player["defense"] = defense
player["speed"] = speed

user = input("유저 이름을 입력해주세요: ")

print()
print(f"✨ {user} 캐릭터 생성 완료! ✨")
print("==========================================")
print(f"캐릭터: {player['job']}")
print(f"체력: {player['hp']}/{player['max_hp']}")
print(f"공격력: {player['attack']}")
print(f"방어력: {player['defense']}")
print(f"속도: {player['speed']}")
print("==========================================")
input("\nEnter를 눌러 게임을 시작하세요...")


# 게임 메인 루프
while player["hp"] > 0:
    clear_screen()
    
    print(f"🎮 {user}의 모험 🎮")
    print(f"현재 체력: {player['hp']}/{player['max_hp']}")
    print()
    print("=== 게임 메뉴 ===")
    print("1. 상태 확인")
    print("2. 슬라임과 전투")
    print("3. 고블린과 전투")
    print("4. 거인과의 전투")
    print("5. 드래곤과 전투")
    print("6. 휴식 (체력 회복)")
    print("7. 게임 종료")
    print()
    
    menu_choice = input("선택하세요: ")
    
    if menu_choice == "1":
        # 상태 확인
        clear_screen()
        print(f"=== {user}의 상태 ===")
        print(f"체력: {player['hp']}/{player['max_hp']}")
        print(f"공격력: {player['attack']}")
        print(f"방어력: {player['defense']}")
        print(f"속도: {player['speed']}")
        print()
        input("Enter를 눌러 메뉴로 돌아가기...")
        
    elif menu_choice in ["2", "3", "4", "5"]:
        # 전투
        if player["hp"] <= 0:
            print("체력이 부족합니다! 먼저 휴식을 취하세요.")
            input("Enter를 눌러 계속...")
            continue
        
        clear_screen()
        
        # 몬스터 선택
        monster_list = ["슬라임", "고블린", "거인", "드래곤"]
        monster_name = monster_list[int(menu_choice) - 2]
        
        print(f"⚔️ {monster_name}이(가) 나타났다!")
        
        # 몬스터 정보
        monster_hp, monster_attack, monster_defense, monster_speed = environment[monster_name]
        current_monster_hp = monster_hp
        
        print(f"{monster_name} - HP:{monster_hp}, ATK:{monster_attack}, DEF:{monster_defense}, SPD:{monster_speed}")
        
        # 속도로 선공 결정
        if player["speed"] >= monster_speed:
            print(f"{user}가 먼저 공격합니다")
            playerfirstatt = True
        else:
            print(f"{monster_name}이 먼저 공격합니다")
            playerfirstatt = False
            
        input("Enter를 눌러서 진행...")
        
        # 전투 루프
        while current_monster_hp > 0 and player["hp"] > 0:
            clear_screen()
            
            print(f"⚔️ 전투 중: {user} VS {monster_name}")
            print("==========================================")
            print(f"{player['job']}의 체력: {player['hp']}/{player['max_hp']}")
            print(f"{monster_name} 체력: {current_monster_hp}/{monster_hp}")
            print("==========================================")
            
            input("Enter를 눌러 공격...")
            
            if playerfirstatt:
                # 플레이어 먼저 공격
                print(f"{user}의 선공!")
                input("공격을 하려면 Enter를 눌러주세요...")
                
                player_damage = max(1, player["attack"] - monster_defense)
                current_monster_hp -= player_damage
                print(f"{user}의 공격 데미지: {player_damage}!")
                
                if current_monster_hp <= 0:
                    print(f"{monster_name}을 물리쳤습니다!")
                    # 몬스터 승리 보상
                    if monster_name=="슬라임":
                        print("체력:+1 방어력: +1 늘어났습니다")
                        player["defense"]+=1
                        player["max_hp"]+=1
                        player["hp"]+=1
                    if monster_name=="고블린":
                        print("공격력: +1 늘어났습니다")
                        player["attack"]+=1
                    if monster_name=="거인":
                        print("공격력: +3, 체력: +5, 방어력: +3 늘어났습니다")
                        player["defense"]+=3
                        player["attack"]+=3
                        player["max_hp"]+=5
                        player["hp"]+=5
                    if monster_name=="드래곤":
                        print("공격력: +5, 체력: +5, 방어력: +5 늘어났습니다")
                        player["defense"]+=5
                        player["attack"]+=5
                        player["max_hp"]+=5
                        player["hp"]+=5
                    input("Enter를 눌러 계속...")
                    break
                
                # 몬스터 반격
                monster_damage = max(1, monster_attack - player["defense"])
                player["hp"] -= monster_damage
                print(f"{monster_name}의 공격 데미지: {monster_damage}!")
                
            else:
                # 몬스터 먼저 공격
                print(f"{monster_name}의 선공!")
                
                monster_damage = max(1, monster_attack - player["defense"])
                player["hp"] -= monster_damage
                print(f"{monster_name}의 공격 데미지: {monster_damage}")
                
                if player["hp"] <= 0:
                    print(f"{user}님의 패배")
                    print("다시 하시려면 재실행 해주세요")
                    input("Enter를 눌러 종료...")
                    break
                
                # 플레이어 반격
                player_damage = max(1, player["attack"] - monster_defense)
                current_monster_hp -= player_damage
                print(f"{user}의 공격 데미지: {player_damage}!")
            
            input("Enter를 눌러 진행")
            
            
    elif menu_choice == "6":
        # 휴식
        clear_screen()
        input("Enter를 눌러 회복...")
        player["hp"] = player["max_hp"]        
        print(f"회복완료! HP: {player['hp']}/{player['max_hp']}")
        input("Enter를 눌러 계속...")
        
    elif menu_choice == "7":
        # 게임 종료
        clear_screen()
        choice_end = input("1= 게임종료 \n2= 메뉴로 돌아가기: ")
        
        if choice_end == "1":
            clear_screen()
            print("게임을 종료합니다")
            break
        elif choice_end == "2":
            continue
        else:
            print("잘못된 선택입니다. 메뉴로 돌아갑니다.")
            input("Enter를 눌러 계속...")
            continue
            
    else:
        clear_screen()
        print("아직 지원하지않는 선택지입니다")
        input("Enter를 눌러 계속...")


clear_screen()
print("게임 종료")
