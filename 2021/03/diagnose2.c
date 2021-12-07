#include <stdio.h>
#include <stdlib.h>

char *toBinary(uint n, uint len) {
  char *binary = (char *)malloc(sizeof(char) * len);
  uint k = 0;
  for (unsigned i = (1 << (len - 1)); i > 0; i = i / 2) {
    binary[k++] = (n & i) ? '1' : '0';
  }
  binary[k] = '\0';
  return binary;
}

int main(int argc, char *argv[]) {
  FILE *fp = fopen("input", "r");
  uint stats[12] = {0};
  uint numbers[1000];
  uint sentinels[12] = {0b1};
  for (uint i = 1; i < 12; i++) {
    sentinels[i] = sentinels[i - 1] << 1;
    stats[i] = 0;
  }

  uint i = 0;
  char strval[15];
  uint count = 0;
  while (fgets(strval, 14, fp) != NULL) {
    numbers[count] = (uint)strtol(strval, NULL, 2);
    for (; i < 12; i++) {
      stats[i] += (sentinels[i] | numbers[count]) == numbers[count];
    }
    i = 0;
    count++;
  }
  // pruint array stats
  // for (uint i = 0; i < 12; i++) {
  //   printf("%d\n", stats[i]);
  // }

  uint oxy = 0;
  uint co2 = 0;
  // Build both numbers and sentinels
  for (i = 0; i < 12; i++) {
    oxy = oxy | (stats[i] > count / 2) << (11 - i);
    co2 = co2 | (stats[i] < count / 2) << (11 - i);
  }
  // Keeps track of the best match
  uint boxy = 0, bco2 = 0;
  uint contador = 0;
  // o is used to walk through the oxygen, c is used to walk through the co2
  for (uint i = 0, o = 0, c = 0, val, omatch, cmatch, increment; i < 1000;) {
    val = numbers[i];

    // Oxygen
    // Compare only the 11 - o bits of val to the 11 - o bits of oxy
    omatch = (oxy >> (11 - o)) == (val >> (11 - o));
    // printf("oxy %d: %s val %d: %s\n", o, toBinary((oxy >> (11 - o)), 12), o, toBinary((val >> (11 - o)), 12));
    boxy = omatch ? val : boxy;
    // If there's a match increment
    o += omatch * !(o == 11);
    // Only increment if there's not a match
    increment = !omatch || o == 11;

    // Co2
    // Compare only the 11 - o bits of val to the 11 - o bits of oxy
    cmatch = (co2 >> (11 - c)) == (val >> (11 - c));
    bco2 = cmatch ? val : bco2;
    // If there's a match increment
    c += cmatch * !(c == 11);
    // Load up the next value when there wasn't a match, or already in the last character
    increment = !cmatch || c == 11;


    i += increment;
    increment = 0;
    contador++;
  }
  printf("Oxy: %s\nCo2: %s\n", toBinary(oxy, 12), toBinary(co2, 12));
  printf("Result: Oxygen:%d - %s , Co2:%d - %s multiplied:%d\n", boxy, toBinary(boxy, 12), bco2, toBinary(bco2, 12), boxy * bco2);

  return 0;
}
