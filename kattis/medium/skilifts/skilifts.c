#include <stdio.h>
#include <stdlib.h>

struct vertex{
	int y;
	int type;
	struct vertex **adj;
};

void merge(struct vertex *left, int leftLen, struct vertex *right, int rightLen)
{
	struct vertex *temp;
	temp = malloc(sizeof(int) * (leftLen + rightLen));
	int currLeft = 0, currRight = 0, currTemp = 0;

	while (currLeft < leftLen && currRight < rightLen){
		if (left[currLeft].y < right[currRight].y)
			temp[currTemp++] = left[currLeft++];
		else
			temp[currTemp++] = right[currRight++];
	}
	while (currLeft < leftLen)
		temp[currTemp++] = left[currLeft++];
	while (currRight < rightLen)
		temp[currTemp++] = right[currRight++];
	
	for (int i = 0; i < leftLen + rightLen; i++)
		left[i] = temp[i];
}

void sort(struct vertex *list, int len)
{

	if (len == 1)
		return;

	struct vertex *left, *right;
	int leftLen, rightLen;
	leftLen = len / 2;
	rightLen = len - leftLen;
	left = list;
	right = list + leftLen;

	sort(left, leftLen);
	sort(right, rightLen);
	merge(left, leftLen, right, rightLen);

}

int main(){
	
	int n;
	struct vertex *vertices;
	vertices = malloc(sizeof(struct vertex)*n);
	int x, y, type;
	scanf("%d",&n);

	for (int i = 0; i < n; i ++){
		scanf("%d %d %d", &x, &y, &type);
		vertices[i].y = y;
		vertices[i].type = type;
	}

	sort(vertices, n);

	struct vertex *temp;
	temp = malloc(sizeof(struct vertex)*n);
	int currTemp, prevTemp;
	int prevStart = -1, currStart = 0;
	currTemp = 1;
	prevTemp = 0;
	temp[0] = vertices[0];

	for (int i = 0; i < n; i++){
		if (temp[prevTemp].y != vertices[i].y){
			prevStart = currStart;
			currStart = i;
			printf("Prev: %d, Curr: %d", prevStart, currStart);
			currTemp = 0;
			prevTemp = -1;
			printf("%d\n",i);
		}
		temp[currTemp++] = vertices[i];
		prevTemp++;
	}

	return 1;
}
