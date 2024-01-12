def cal_min(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m

def check_empty_room(enter_time, rooms):
    for idx, room_time in enumerate(rooms):
        if enter_time >= room_time:
            return idx
    return -1
        
def solution(book_time):
    rooms = [0]
    book_times = sorted(book_time, key=lambda x:x[0])
    for book_time in book_times:
        enter_time = cal_min(book_time[0])
        finish_time = cal_min(book_time[1])
        
        room_idx = check_empty_room(enter_time, rooms)
        if room_idx == -1: # 방이 없다면
            rooms.append(finish_time+10)
        else: # 방이 있다면
            rooms[room_idx] = finish_time+10
    return len(rooms)