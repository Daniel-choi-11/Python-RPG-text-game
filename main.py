import os
from googletrans import Translator

'''
처음에 캐릭터 정보 만들기
4개정도
캐릭터 직업 이름 : 스탯 4개 체력 공격력 방어력 ..
아이템 : 공격력 + 방어력 +
'''
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# 1. 체력(1-100)   2. 공격력(1-100)   3.방어력(1-100)   4.속도(1-5)
jobs={
    "전사":(70, 60, 60, 3),
    "도적":(35, 90, 20, 5),
    "궁수":(55, 75, 40, 4),
    "방패병":(100, 50, 90, 1)
}

player={}

# 1. 체력   2. 공격력   3.방어력   4.속도(1-10)
environment={
    "슬라임":(10, 5, 5, 1),
    "고블린":(20, 10, 5, 3),
    "거인":(400, 40, 0, 2),
    "드래곤":(500, 50, 30, 5),
}

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
choice=input("1~4 중 하나를 선택해주세요 (번호입력):")

if choice=="1":
    print("전사를 선택하셨습니다")
    job="전사"
elif choice=="2":
    print("도적을 선택하셨습니다")
    job="도적"
elif choice=="3":
    print("궁수를 선택하셨습니다")
    job="궁수"
elif choice=="4":
    print("방패병을 선택하셨습니다")
    job="방패병"
else:
    print("1~4에 있는 숫자만 입력해주세요!")
os.system("clear")

hp, attack, defense, speed = jobs[job]
player["job"] = job
player["hp"] = hp
player["max_hp"] = hp
player["attack"]= attack
player["defense"]= defense
player["speed"]= speed

user=input("유저 이름을 입력해주세요:")
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
        clear_screen()
        print(f"=== {user}의 상태 ===")
        print(f"체력: {player['hp']}/{player['max_hp']}")
        print(f"공격력: {player['attack']}")
        print(f"방어력: {player['defense']}")
        print(f"속도: {player['speed']}")
        print()
        input("Enter를 눌러 메뉴로 돌아가기...")
        
    elif menu_choice in ["2", "3", "4", "5"]:
        if player["hp"] <= 0:
            print("체력이 부족합니다! 먼저 휴식을 취하세요.")
            input("Enter를 눌러 계속...")
            continue
        
        clear_screen()
        
        monster_list = ["슬라임", "고블린", "거인", "드래곤"]
        monster_name = monster_list[int(menu_choice) - 2]
        
        print(f"⚔️ {monster_name}이(가) 나타났다!")
        
    elif menu_choice== "6":
        if player["hp"]<0:
            player["hp"] = player["max_hp"]
            print("회복완료")
            print("Enter를 눌러 계속...")
        else:
            print("체력이 0이하일때만 사용가능합니다")
    elif menu_choice== "7":
        print("정말로 게임종료를 하시겠습니까?")
        input("Enter를 눌러 진행하세요:")
        break






# 몬스터가 일정 확률로 공격력 버프/너프. 
# 유저도 일정확률로 공격력 버프/너프
# 공격, 수비 공격 수비 이런식

