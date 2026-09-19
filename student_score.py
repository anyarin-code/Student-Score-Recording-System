print("                    ")

print(" ระบบบันทึกคะแนนนักเรียน ")
print("         ")

stdname = input(" ชื่อนักเรียน: ")
stdID = int(input(" รหัสนักศึกษา: "))

again = "y"

while again == "y":
    sj = input(" วิชา: ")
    score = int(input(" คะแนน: ")) 

    if score < 0 or score > 100:
        print(" คะแนนไม่ถูกต้อง! ")
    else:
        if score >= 80:
            grade = "A"
        elif score >= 70:
            grade = "B"
        elif score >= 60:
            grade = "C"
        elif score >= 50:
            grade = "D"
        else:
            grade = "F"

        if score >= 50:
            result = "ผ่าน"
        else:
            result = "ไม่ผ่าน"

        print("            ")
        print(" |ผลการเรียน| ")
        print("            ")
        print(" ชื่อ: ", stdname)
        print(" รหัสนักศึกษา: ", stdID)
        print(" วิชา: ", sj)
        print(" คะแนน: ", score)
        print(" เกรด: ", grade)
        print(" ผลการเรียน: ", result)
        print("            ")
    again = input(" ต้องการเพิ่มวิชาอีกไหม: ")
    print("                 ")







