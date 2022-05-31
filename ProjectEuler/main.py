import program1
import program2
import program3
import program4
import program5
import program6
import program7
import program8
import program9
import program10
import program11
import program12
import program13
import program14
import program15
import program16
import program17
import program18
import program19
import program20
import program21
import program22
import program23
import program24
import program25
import program26
import program27
import program28
import program29
import program30
import program31
import program32
import program33
import program34
import program35
import program36
import program37
import program38
import program39
import program40

def generate_files(start, stop):
    for i in range(start,stop+1):
        with open(f"program{i}.py","w") as file:
            file.write(f"import utils\n\n#\n\ndef task(n):\n\tpass\n\ndef program():\n\tprint(\"Answer: \",task(100))")

def generate_ref(start, stop):
    for i in range(start, stop+1):
        print(f"#program{i}.program()")

def generate_imports(start, stop):
    for i in range(start, stop+1):
        print(f"import program{i}")

if __name__ == '__main__':
    #program1.program()
    #program2.program()
    #program3.program()
    #program4.program()
    #program5.program()
    #program6.program()
    #program7.program()
    #program8.program() # TODO
    #program9.program()
    #program10.program()
    #program11.program() # TODO
    #program12.program()
    #program13.program()
    #program14.program()
    program15.program()
    #program16.program()
    #program17.program()
    #program18.program()
    #program19.program()
    #program20.program()
    #program21.program()
    #program22.program()
    #program23.program()
    #program24.program()
    #program25.program()
    #program26.program()
    #program27.program()
    #program28.program()
    #program29.program()
    #program30.program()
    #program31.program()
    #program32.program()
    #program33.program()
    #program34.program()
    #program35.program()
    #program36.program()
    #program37.program()
    #program38.program()
    #program39.program()
    #program40.program()
    #generate_files(8, 40)
    #generate_ref(8,40)
    #generate_imports(8,40)



