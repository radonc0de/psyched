import os
import sys

def main():
    if len(sys.argv) > 1:
        #help command
        if sys.argv[1] == '--help':
            command_list()

        #load schedule
        elif sys.argv[1] == '--load' or sys.argv[1] == '-l':
            if len(sys.argv) > 2:
                if sys.argv[2][-5:] == '.yaml': filename =  sys.argv[2][:-5]
                else: filename = sys.argv[2]
                if (os.path.exists("%s.yaml" % filename)):
                    interactive_mode(filename)
                else:
                    print("psyched: cannot open file '%s.yaml': No such file" % filename)
                    sys.exit()

        #load and copy to new schedule
        elif sys.argv[1] == '--load_temp' or sys.argv[1] == '-t':
            if len(sys.argv) > 3:
                if sys.argv[2][-5:] == '.yaml': filename =  sys.argv[2][:-5]
                else: filename = sys.argv[2]
                if (os.path.exists("%s.yaml" % filename)):

                    print(filename)
                else:
                    print("psyched: cannot open file '%s': No such file" % sys.argv[2])
                    sys.exit()

        #create new schedule
        elif sys.argv[1] == '--new' or sys.argv[1] == '-n':
            if len(sys.argv) > 2:
                if (os.path.exists(sys.argv[2]) or (os.path.exists("%s.yaml" % sys.argv[2]))):
                    print("psyched: cannot create file '%s': File already exists" % sys.argv[2])
                    sys.exit()
                else:
                    print(sys.argv[2])

        # handle error
        else:
            print("psyched: unknown command")
            print("Try 'psyched --help' for command list.")
            sys.exit()
    else:
        print("psyched: missing command")
        print("Try 'psyched --help' for command list.")
        sys.exit()

def interactive_mode(schedulename):
    command = input("Enter command or 'help' and press return: ")
    if command == 'help':
        '''help screen'''
    elif command == 'add':
        eventname = input("Enter new event name:")
        eventdays = input("Enter new event days (Ex. MonTueWedThuFri):")
        eventtimes = input("Enter new event times (Ex. 8-8.30:")
        eventcolor = input("Enter new event category:")
        new_event(schedulename, eventname, eventdays, eventtimes, eventcolor)
        interactive_mode(schedulename)
    elif command == 'compile':
        compile_schedule(schedulename)
        interactive_mode(schedulename)
    elif command == 'exit':
        sys.exit()



def new_event(filename, name, days, time, color):
    with open('%s.yaml' % filename, "a") as f:
        f.write('\n- name: %s \n' % name)
        f.write('  days: %s \n' % days)
        f.write('  time: %s \n' % time  )
        f.write('  color: "%s" \n' % color)

def view_schedule(filename):
    with open(filename, "r") as f:
        data = f.read().splitlines()
    print(data)

def command_list():
    print(
'''Usage: psyched [OPTION]... SCHEDULENAME...
Usage: psyched -t EXISTING_SCHEDULE... NEW_SCHEDULE...
Mandatory arguments:
-l, --load                  load a schedule
-n, --new                   create a new schedule
-t, --loadtemp              create a new schedule using another as a template
    --help          display this help and exit
Full documentation <https://github.com/radonc0de/psyched-cli>'''
    )

def compile_schedule(filename):
    os.system("pdfschedule -CMp %s.yaml %s.pdf" % (filename, filename))

if __name__ == "__main__":
    main()
