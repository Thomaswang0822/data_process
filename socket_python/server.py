#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
!jupyter nbextension enable --py widgetsnbextension --sys-prefix
!jupyter serverextension enable voila --sys-prefix
"""
print("Server starting......")


# In[2]:


import socket
import os
import threading
import time
import easygui as eg


# In[ ]:


savepath = eg.diropenbox(title="Choose place to save file")
if not os.path.exists(savepath):
    os.mkdir(savepath)


# In[ ]:


class Server:
    def __init__(self):
        # Create socket
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # get host name
        self.host = socket.gethostname()
        print(self.host)
        
        # set prot
        self.port = 3636
        
        # bind address
        self.server.bind( ("169.254.4.254", self.port) )
        
        # set Max connection
        self.server.listen(12)
        print("Server online, waiting for client connection")
        
    def server100(self):
        while 1:
            # set client connection
            client, addr = self.server.accept()
            print(f'client: {str(addr)}, connected to the server')
            msg = f'connected to host {self.host}. \r\n'
            client.send(msg.encode('utf-8'))
            
            # Create a threading for client after connection
            t1 = threading.Thread(self.taskfilethread(client))
            # set threading guard
            t1.setDaemon(True)
            # start
            t1.start()
            
    def taskfilethread(self, client):
        # recv file name and size
        filename = client.recv(1024)
        filesize = client.recv(1024)
        # decode them
        filename = filename.decode()
        filesize = int.from_bytes(filesize, byteorder='big')
        
        # recv file
        try:
            f = open(savepath + "/" + filename, 'wb')
            size = 0
            start_t = time.time()
            while 1:
                # recv data
                f_data = client.recv(1024)
                
                if f_data:
                    f.write(f_data)
                    size += len(f_data)
                    if time.time() - start_t == 0:
                        time.sleep(0.5)
                    speed = size/(time.time() - start_t)
                    print("Downloading: {}% complete, speed: {} MB/s". format(size/filesize*100, float(size/1024/1024)))
                else:
                    break              
        except Exception as e:
            print("error when receiving: ", e)
        else:
            print("Downloading {} complete".format(filename))
        finally:
            f.flush()
            f.close()
            return
            
if __name__ == '__main__':
    server = Server()
    server.server100()
    server.close()


# In[ ]:




