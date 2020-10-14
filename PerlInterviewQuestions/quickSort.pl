use strict;
use warnings;
use Data::Dumper;

sub quickSort {
    my $L = shift();
    my $first = shift;
    my $last = shift;

    if ($first < $last) {
        my $splitPoint = partition($L, $first, $last);
        quickSort($L, $first, $splitPoint - 1);
        quickSort($L, $splitPoint + 1, $last);
    }
}

sub partition {
    my $L = shift();
    my $first = shift;
    my $last = shift;

    my $pivotVAlue = $L->[$last];
    my $i = $first - 1;

    for (my $j = $first; $j <= $last; $j++) {
        if ($L->[$j] <= $pivotVAlue) {
            $i++;
            my $temp = $L->[$j];
            $L->[$j] = $L->[$i];
            $L->[$i] = $temp;
        }
    }

    return $i;
}

my @L = (5, 2, 6, 4, 7, 8, 1, 10, 14, 23, 54, 33);
$Data::Dumper::Indent = 0;
print Dumper \@L;
print "\n";
quickSort(\@L, 0, $#L);
print Dumper \@L;

