#include <iostream>
#include <string>

using namespace std;

string replace_amp_lt_gt(string input) {
    size_t pos = 0;
    while ((pos = input.find("&", pos)) != string::npos) {
        input.replace(pos, 1, "&amp;");
        pos += 5;
    }
    pos = 0;
    while ((pos = input.find("<", pos)) != string::npos) {
        input.replace(pos, 1, "&lt;");
        pos += 4;
    }
    pos = 0;
    while ((pos = input.find(">", pos)) != string::npos) {
        input.replace(pos, 1, "&gt;");
        pos += 4;
    }
    return input;
}

int main() {
    cout << "Ampersand:" << endl;
    string amp_org = "What the he&&y";
    cout << "Original: " << amp_org << endl;
    string amp_alt = replace_amp_lt_gt(amp_org);
    cout << "Altered: " << amp_alt << endl << endl;

    cout << "Less than:" << endl;
    string lt_org = "What the he<<y";
    cout << "Original: " << lt_org << endl;
    string lt_alt = replace_amp_lt_gt(lt_org);
    cout << "Altered: " << lt_alt << endl << endl;

    cout << "Greater than:" << endl;
    string gt_org = "What the he>>y";
    cout << "Original: " << gt_org << endl;
    string gt_alt = replace_amp_lt_gt(gt_org);
    cout << "Altered: " << gt_alt << endl << endl;

    return 0;
}