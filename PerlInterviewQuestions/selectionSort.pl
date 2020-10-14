use strict;
use warnings;
use Data::Dumper;

sub selectionSort {
    my $L = shift();
    for (my $i = 0; $i < $#$L; $i++) {
        for (my $j = $i; $j <= $#$L; $j++) {
            if ($L->[$i] > $L->[$j]) {
                my $temp = $L->[$i];
                $L->[$i] = $L->[$j];
                $L->[$j] = $temp;
            }
        }
    }
}

my @L = (5, 2, 6, 4, 7, 8, 1, 10, 14, 23, 54, 33);
$Data::Dumper::Indent = 0;
print Dumper \@L;
selectionSort(\@L);
print Dumper \@L;
