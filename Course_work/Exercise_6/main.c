#include "utility.h"
#include <stdio.h>
#include <string.h>

int main() {
    printf("Replace &, <, > function:\n");
    char* amp_org = "& < >";
    printf("Original: %s\n", amp_org);
    char* amp_alt = replace_amp_lt_gt(amp_org);
    printf("Altered: %s\n\n", amp_alt);
    free(amp_alt);
}
