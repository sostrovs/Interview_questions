use strict;
use warnings;
use Data::Dumper;

sub getPeak {
    my $L = shift();
    my $first = shift;
    my $last = shift;

    my $mid = int(($first+$last)/2);
    if($$L[$first] <= $$L[$mid] && $$L[$mid] <= $$L[$last]) {
        return $last;
    }

    if($$L[$first] >= $$L[$mid] && $$L[$mid] >= $$L[$last]) {
        return $first;
    }

    my $left = getPeak(\@$L, $first, $mid-1);
    my $right = getPeak(\@$L, $mid+1, $last);

    if($$L[$left] <= $$L[$mid] && $$L[$mid] <= $$L[$right]) {
        return $right;
    }

    if($$L[$left] >= $$L[$mid] && $$L[$mid] >= $$L[$right]) {
        return $left;
    }

    return $mid;
}

sub findPeak {
    my $L = shift();
    return getPeak(\@$L, 0, $#$L);
}

my @L = (1, 2, 3, 4, 7, 8, 25, 13, 11, 1);
$Data::Dumper::Indent = 0;
print Dumper \@L;
print("\n");
print(findPeak(\@L));