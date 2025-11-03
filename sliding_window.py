def sliding_window():
    w = int(input("Enter window size: "))
    f = int(input("Enter number of frames: "))

    frames = []
    print("Enter the frame numbers:")
    for i in range(f):
        frames.append(int(input(f"Frame {i+1}: ")))

    print("\nWith sliding window protocol, the frames will be sent in the following manner (assuming no corruption):\n")

    for i in range(0, f, w):
        print(f"Sending frames: {frames[i:i+w]}")
        print(f"Waiting for acknowledgment of frames {frames[i:i+w]}\n")

    print("All frames have been successfully sent and acknowledged.")

sliding_window()
