#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
  FILE *fp = fopen("input", "r");
  char dir;
  int mag;
  int pos[3] = {0, 0, 0};
  // Consume all left whitespace, consume 1 char, consume a non captured
  // string, consume a dicgit (which also consumes the leading whitespace).
  while (fscanf(fp, " %1c%*s%d", &dir, &mag) != EOF) {
    switch (dir) {
    case 'f':
      pos[0] += mag;
      break;
    case 'u':
      pos[1] -= mag;
      break;
    case 'd':
      pos[1] += mag;
      break;
    default:
      printf("Invalid direction: %c\n", dir);
      exit(1);
    }
  }
  printf("Final position x:%i, y:%i, x * y = %i\n", pos[0], pos[1], pos[0] * pos[1]);
  return 0;
}
