import threading

status = True



def manual_routing():
  print("d")

def route():
  while status:
    print("h")

# Create and start threads
manual_routing_thread = threading.Thread(target=manual_routing)
route_thread = threading.Thread(target=route)

manual_routing_thread.start()
route_thread.start()


# Wait for both threads to finish (optional)
manual_routing_thread.join()
route_thread.join()

