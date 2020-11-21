def get_identifier(planes, due, call):
    plane = planes.pop(0)
    if plane.upper() == 'ZZZ':
        print('no planes in the queue')
    else:
        print(
            f"Next plane: {plane}\n"
            f"Due: {due.pop(0)}\n"
            f"Call: {call.pop(0)}\n"
            f"planes left in the queue {len(planes)-1}")


plane = ['asd123', 'sds456', 'zzz']
due = [956, 955]
call = [850, 875]
get_identifier(plane, due, call)
