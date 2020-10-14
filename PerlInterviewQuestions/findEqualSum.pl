use strict;
use warnings;
use Data::Dumper;

sub getEqualSum {
    my $L = shift();
    my $first = shift;
    my $last = shift;
    my $M = shift;
    my $mid = int(($first + $last) / 2);

    if (exists($$M{$mid})) {
        $mid++;
        if (exists($$M{$mid})) {
            $mid -= 2;
            if (exists($$M{$mid})) {
                return 'No equal sum';
            }
        }
    }

    $$M{$mid} = undef;

    my $sum1 = eval join '+', @$L[0 .. $mid];
    my $sum2 = eval join '+', @$L[$mid + 1 .. $#$L];

    if ($sum1 == $sum2) {
        return $mid;
    }
    else {
        if ($sum1 < $sum2) {
            return getEqualSum(\@$L, $mid + 1, $#$L, \%$M);
        }
        else {
            return getEqualSum(\@$L, 0, $mid, \%$M);
        }
    }
}

sub findEqualSum {
    my $L = shift();
    my %M = ();
    return getEqualSum(\@$L, 0, $#$L, \%M);
}

my @L = (1, 5, 8, 9, 1, 3, 3, 3, 4, 4, 5, 2);
$Data::Dumper::Indent = 0;
print Dumper \@L;
print("\n");
print(findEqualSum(\@L));