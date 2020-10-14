use strict;
use warnings;
use Data::Dumper;

sub getPermuationSets {
    my $str = shift;
    my @L = split("", $str);
    my @P = ();
    for(my $i = 0; $i <= $#L; $i++) {
        for(my $j = 0; $j < $#L; $j++) {
            push(@P, join("", @L));
            my $temp = $L[$j];
            $L[$j] = $L[$j+1];
            $L[$j+1] = $temp;
        }
    }
    return @P;
}

my @permutation = getPermuationSets("abc");
$Data::Dumper::Indent = 0;
print Dumper \@permutation;
