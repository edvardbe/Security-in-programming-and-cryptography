#include "utility.h"
#include <assert.h>
#include <string.h>

int main() {
    assert(strcmp(replace_amp_lt_gt(""), "") == 0);
    assert(strcmp(replace_amp_lt_gt("& < >"), "&amp; &lt; &gt;") == 0);
    assert(strcmp(replace_amp_lt_gt("unaltered"), "unaltered") == 0);
    assert(strcmp(replace_amp_lt_gt("altered &"), "altered &amp;") == 0);
    // Additional tests
}
