#include <iostream>
#include <string>
#include "ll.h"



LinkedList::Node::Node(int x)
{
    data = x;
    next = nullptr;
}


LinkedList::LinkedList()
{
    Node *head = nullptr;
}


LinkedList::LinkedList(const LinkedList &L){

}


LinkedList::~LinkedList(){

}

void LinkedList::addNode(int x) {
    Node * current = new Node(x);
    Node * temp = head;
    if (temp == nullptr) {
        head = current;
        return ;
    }
    while (temp->next != nullptr) {
        temp = temp->next;
    }
    temp->next = current;
}

void LinkedList::deleteNode(int x) {
    Node * prev = nullptr;
    Node * current = head;
    while (current != nullptr && current->data != x) {
        prev = current;
        current = current->next;
    }
    if (current == nullptr) {
        return ;
    }
    if (prev == nullptr) {
        head = current->next;
        delete current;
        return ;
    }
    prev->next = current->next;
    delete current;
}
string LinkedList::toString() {
    string s = "";
    Node * temp = head;
    while (temp != nullptr) {
        s += to_string(temp->data);
        temp = temp->next;
    }
    return s;
}

void LinkedList::clear(){
    Node * temp = nullptr;
    while (head != nullptr) {
        temp = head;
        head = head->next;
        delete temp;
    }
}

ostream &operator<<(ostream &stream, LinkedList &L){
    return stream << L.toString();
}

bool operator==( LinkedList& A, const LinkedList& B ){

}




