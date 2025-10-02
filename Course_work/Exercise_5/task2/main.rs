fn replace_amp_lt_gt(mut input: String) -> String {
    input = input.replace("&", "&amp;");
    input = input.replace("<", "&lt;");
    input = input.replace(">", "&gt;");
    return input;
}

fn main(){

    println!("Ampersand:");
    let amp_org = String::from("What the he&&y");
    println!("Original: {}", amp_org);
    let amp_alt: String = replace_amp_lt_gt(amp_org);
    println!("Altered: {}\n", amp_alt);


    println!("Less than:");
    let lt_org = String::from("What the he<<y");
    println!("Original: {}", lt_org);
    let lt_alt: String = replace_amp_lt_gt(lt_org);
    println!("Altered: {}\n", lt_alt);

    println!("Greater than:");
    let gt_org = String::from("What the he>>y");
    println!("Original: {}", gt_org);
    let gt_alt: String = replace_amp_lt_gt(gt_org);
    println!("Altered: {}\n", gt_alt);

}