
void merge(int *left, int leftLen, int *right, int rightLen)
{
	int *temp;
	temp = malloc(sizeof(int) * (leftLen + rightLen));
	int currLeft = 0, currRight = 0, currTemp = 0;

	while (currLeft < leftLen && currRight < rightLen){
		if (left[currLeft] < right[currRight])
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

void sort(int *list, int len)
{

	if (len == 1)
		return;

	int *left, *right, leftLen, rightLen;
	leftLen = len / 2;
	rightLen = len - leftLen;
	left = list;
	right = list + leftLen;

	sort(left, leftLen);
	sort(right, rightLen);
	merge(left, leftLen, right, rightLen);

}
