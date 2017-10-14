// AlgoritmCPP.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

const tree* null = NULL;
struct tree {
	tree* parent = NULL;
	tree* child[2] = { NULL };
	int value = 0;
	tree(int x, tree* parent1) {
		value = x;
		parent = parent1;
	}
};

void insert(tree* parent, tree*& node, int value) {
	if (node == NULL) {
		node = new tree(value, parent);	//새로운 노드를 만들고
		return;//종료
	}
	if (value == node->value) //같이 중복된다면
		return; //종료
	insert(node, node->child[value > node->value], value);
	//삽입할 값이 노드의 값보다 크면 node->child[0] 탐색
	//작다면 node->child[1] 탐색
}
tree*& find(tree*& node, int value) {
	if (node == NULL) // 노드가 비어있다면
		return null; //NULL반환
	if (value == node->value) //노드의 값이 검색할 값과 같다면
		return node;//검색된 노드의 위치 반환
}

int main()
{
    return 0;
}

