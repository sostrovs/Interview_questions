use strict;
use warnings;
use Data::Dumper;

sub displayList {
    my $L = shift();

    for (my $i = 0; $i < scalar(@$L); $i++) {
        for (my $j = 0; $j < scalar(@{$$L[$i]}); $j++) {
            print $$L[$i][$j] . " ";
        }
        print "\n";
    }
}

sub generateMatrix {
    my $n = shift;
    my $length = shift;
    my @L = ();
    for (my $i = 0; $i < $length; $i++) {
        my @A = ();
        for (my $j = 0; $j < $n; $j++) {
            push(@A, 0);
        }
        push(@L, \@A);
    }
    return @L;
}

sub numberOfPaths {
    my $n = shift;
    my $length = shift;
    my @L = generateMatrix($n, $length);
    for (my $i = 0; $i < scalar(@L); $i++) {
        for (my $j = 0; $j < scalar(@{$L[$i]}); $j++) {
            if (($i == 0 && $j != 0) || ($i != 0 && $j == 0)) {
                $L[$i][$j] = 1;
            }

            if ($i != 0 && $j != 0) {
                $L[$i][$j] = $L[$i - 1][$j] + $L[$i][$j - 1];
            }
        }
    }
    return @L;
}

my @L = numberOfPaths(4, 5);
displayList(\@L);