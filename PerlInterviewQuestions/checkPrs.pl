use strict;
use warnings;

sub checkPrs {
    die "Wrong number of args" if (scalar(@_) != 1);
    my $mystr = $_[0];
    my @stack = ();
    my %s = ("{" => undef, "(" => undef, "[" => undef);
    my %d = ("}" => "{", ")" => "(", "]" => "[");
    foreach my $char (split('', $mystr)) {
        if (exists $s{$char}) {
            push(@stack, "$char");
        }
        if (exists($d{$char})) {
            if ($#stack + 1 == 0) {
                return "False";
            }
            else {
                if (exists $d{$char}) {
                    pop(@stack)
                }
            }
        }
    }
    $#stack + 1 == 0 ? return "True" : return "False";
}

print(checkPrs("((())") . "\n");
print(checkPrs("((()))") . "\n");
print(checkPrs("[((()))]") . "\n");
print(checkPrs("}((())") . "\n");
