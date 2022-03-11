# 프린터

from queue import PriorityQueue, Queue

def solution(priorities, location):
    answer = 0
    pq=PriorityQueue()
    q=Queue()
    
    for i in range(len(priorities)):
        pq.put(-priorities[i])
        q.put([-priorities[i],i])
    
    for i in range(pq.qsize()):
        answer+=1
        val=pq.get()
        tval,ti=q.get()
        
        while tval!=val:
            q.put([tval,ti])
            print(tval,ti)
            tval,ti=q.get()
        
        if ti==location:
            return answer
        

