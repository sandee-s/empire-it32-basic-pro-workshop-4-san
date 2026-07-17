gang_members = []
def add_member(name,age,gang):
    new_member = {
        "name" : name
        ,"age"  : age
        ,"gang" : gang
        }
    gang_members.append(new_member)

while True :
    choice = int(input("ต้องการทำอะไร(1)เพื่อเพิ่มสมาชิก(2)เพื่อดูสมาชิกทั้งหมด(อย่างอื่น)เพื่อออก:"))
    if choice == 1 :
        name = input("ชื่ออะไร :")
        age = int(input("อายุเท่าไหร่ :"))
        gang = input("ชื่อแก๊งอะไร :")
        add_member(name,age,gang)
        print("เพิ่มข้อมูลสำเร็จแล้ว")
    elif choice == 2 :
        print(gang_members)
    else :
        print("quiting")