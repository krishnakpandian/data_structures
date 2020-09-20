#include<iostream>
#include<string>

#ifndef LinkedList_H_INCLUDE_
#define LinkedList_H_INCLUDE_

using namespace std;
class LinkedList{

private:

   struct Node{
      int data;
      Node* next;
      Node* prev;
      Node(int x);
   };
   Node* head;

public:

   LinkedList();

   LinkedList(const LinkedList& L);

   ~LinkedList();

   void addNode(int x);

   void deleteNode(int x);

   void clear();

   string toString();

   friend std::ostream& operator<<( std::ostream& stream, LinkedList& L );

   friend bool operator==( LinkedList& A, const LinkedList& B );

};


#endif
