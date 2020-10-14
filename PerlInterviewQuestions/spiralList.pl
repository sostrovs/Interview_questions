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

sub generateList {
    my $n = shift;
    my $length = shift;
    my @L = ();
    for (my $i = 1; $i <= $n; $i += $length) {
        my @A = ();
        for (my $j = $i; $j < $i + $length; $j++) {
            push(@A, $j);
        }
        push(@L, \@A);
    }
    return @L;
}

sub getSpiralList {
    my $L = shift();
    my @S = ();
    my $sr = 0;
    my $sc = 0;
    my $er = scalar @$L;
    my $ec = scalar @{$$L[0]};

    while ($sc < $ec) {
        for (my $i = $sc; $i < $ec; $i++) {
            push(@S, $$L[$sr][$i]);
        }
        $sr++;
        last if ($sr == $er);

        for (my $i = $sr; $i < $er; $i++) {
            push(@S, $$L[$i][$ec - 1]);
        }
        $ec--;
        last if ($sc == $ec);

        for (my $i = $ec - 1; $i > $sc - 1; $i--) {
            push(@S, $$L[$er - 1][$i]);
        }
        $er--;
        last if ($sr == $er);

        for (my $i = $er - 1; $i > $sr - 1; $i--) {
            push(@S, $$L[$i][$sc]);
        }
        $sc++;
    }

    return(@S);
}

my @L = generateList(20, 5);
$Data::Dumper::Indent = 0;
print Dumper \@L;
print "\n";
displayList(\@L);
print "\n";
my @spiralList = getSpiralList(\@L);
print Dumper \@spiralList;

