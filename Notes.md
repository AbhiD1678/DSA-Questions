## Review of Big O

O(1),O(log n) best as they take least number of operations,when the number of operations doesnot depend on n

O(n) for a single loop

O(nlogn)

O(n^2),this for loop within loop


## LinkedList

class Node {
  constructor(value){
    this.value=value
    this.next=null
}

class LinkedList {
  constructor(value){
    New_Node = new Node(value)
    this.head = New_Node
    this.tail=this.head
    this.length=1
  }
 }
 
 ## Methods for linkedlist
 
 # Push Method
 It is used to push items in linkedlist from rightside,O(1) operation
 
 class Node{
  constructor(value){
    this.value=value
    this.next=null
    }
   }
  
 class LinkedList {
  constructor(value){
    newNode=new Node(value}
    this.head=newNode
    this.tail=this.head
    this.length=1
    }
   push(value){
    const newNode= new Node(value)
    if(!this.head){
      this.head=newNode
      this.tail=newNode
      }
     else{
      this.tail.next=newNode
      this.tail=newNode
      }
      this.length++
      return this 
      }
      }
    
    #Pop method
    
