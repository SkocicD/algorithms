#include <stdio.h>

struct cart {
	int left;
	int right;
};

int main()
{
	struct cart a;
	a.right = 1;
	a.left = 2;
	printf("%d\n", a.right);

}

int getCartCounts(){

}
