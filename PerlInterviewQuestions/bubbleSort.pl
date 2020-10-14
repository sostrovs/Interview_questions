use strict;
use warnings;
use Data::Dumper;

sub bubbleSort {
    my $L = shift();
    for (my $i = 0; $i < $#$L; $i++) {
        for (my $j = 0; $j < $#$L; $j++) {
            if ($L->[$j] > $L->[$j + 1]) {
                my $temp = $L->[$j];
                $L->[$j] = $L->[$j + 1];
                $L->[$j + 1] = $temp;
            }
        }
    }
}

my @L = (5, 2, 6, 4, 7, 8, 1, 10, 14, 23, 54, 33);
$Data::Dumper::Indent = 0;
print Dumper \@L;
bubbleSort(\@L);
print Dumper \@L;