#include <stdio.h>
#include <stdlib.h>
#define SIZE 4
int ind(int i)
{
    if (i < 0)
        return i + SIZE;
    else if (i >= SIZE)
        return i - SIZE;
    else
        return i;
}

int main (int argc, char *argv[])
{
  int values[SIZE] = {-1, -1, -1, -1};
  int increments = 0;
  int decrements = 0;
  int previous = 0;
  int current = 0;
  char charint[10];
  FILE *fp = fopen("input", "r");
  int slider = 0;
  int count = 0;
  int ok = 0;
  while (1) {
    count++;
    ok = count >= SIZE;
    if (fgets(charint, 10, fp) == NULL) {
      printf("At the end the counts %d\n", count);
      printf("Increments: %d, decrements: %d\n", increments, decrements);
      break;
    }
    values[slider] = atoi(charint);
    // TODO: I WANT NO BRANCHES1!!!!!!!
    if (ok) {
      // Print each of the previous used indexes
      printf("%d %d %d %d\n", slider, ind(slider - 1), ind(slider - 2), ind(slider - 3));
      current = values[slider] + values[ind(slider - 1)] + values[ind(slider - 2)];
      previous = values[ind(slider - 1)] + values[ind(slider - 2)] + values[ind(slider - 3)];
      increments += ok * current > previous;
      decrements += ok * previous > current;
      printf("Window: %d %d %d %d pre: %d, curr: %d\n", values[0], values[1], values[2], values[3], previous, current);
    }
    slider++;
    slider -= (slider == SIZE) * SIZE;
  }
  return 0;
}
