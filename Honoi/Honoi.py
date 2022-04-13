count = 0

def move_disk(n, src, dest, temp):
    global count
    if n == 0:
        return
    else:
        move_disk(n-1, src, temp, dest)
        print("Move Disk", n, "from", src, "to", dest)
        count += 1
        move_disk(n-1, temp, dest, src)



def main():


    move_disk(20, 'A', 'C', 'B')
    print("Completed in ", str(count), " moves.")

main()