# Review of Big O

O(1),O(log n) best as they take least number of operations,when the number of operations doesnot depend on n

O(n) for a single loop

O(nlogn)

O(n^2),this for loop within loop


# LinkedList

```
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
 ```
 
 ## Methods for linkedlist
 
 ### Push Method
 It is used to push items in linkedlist from rightside,O(1) operation
 
```
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
 ```
    
### Pop method
It is used to remove the right most item and set the item before it as tail,it is O(n) method
```
pop (){
  if(!this.head) return undefined
  let pre = this.head
  let temp = this.head
  while(temp.next){
    pre=temp
    temp=temp.next
    }
   this.tail=pre
   this.tail.next = null
   this.length--
   if(this.length===0){
    this.head=null
    this.tail=null
    }
    return temp
    }
```
### Unshift method
This method is used to add items to a linkedlist from leftside and set it as head.
```
unshift (){
  const newNode=new Node(value)
  if(!this.head){
    this.head=newNode
    this.tail=newNode
    }
   else{
    newNode.next=this.head
    this.head=newNode
    }
    this.length++
    return this
}
```
### Shift method
This method is used to remove the this.head in the linkedlist and it is done by assigning temp=head,head.next as head and removing temp
```
shift (){
  if(!this.head) return undefined
  let temp=this.head
  this.head=this.head.next
  temp.next=null
  this.length--
  if(this.length===0){
  this.tail=null
  }
  return temp
}
