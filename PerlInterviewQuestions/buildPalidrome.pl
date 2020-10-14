use strict;
use warnings;
use Data::Dumper;

sub isPalidrome {
    my $str = shift;
    my @L = split("", $str);
    for (my $i = 0; $i < ($#L + 1) / 2; $i++) {
        if ($L[$i] ne $L[$#L - $i]) {
            return 0;
        }
    }
    return 1;
}

sub buildPalidrome {
    my $str = shift;
    my $new_str = "";
    my @L = split("", $str);
    for (my $i = 0; $i < length($str); $i++) {
        my $sub_str = substr($str, $i - length($str));
        if (isPalidrome($sub_str)) {
            return $str . $new_str
        }
        else {
            $new_str = $L[$i] . $new_str;
        }
    }
}

my $str = "label";
print("$str\n");
my $pal = buildPalidrome($str);
print($pal);
$str = "plaba";
print("\n$str\n");
$pal = buildPalidrome($str);
print($pal);

print("\n");
print(substr($pal, 1,2));
