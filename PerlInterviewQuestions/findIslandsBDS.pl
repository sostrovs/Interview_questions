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
    my @L = (
        [ 1, 1, 2, 3, 3 ],
        [ 1, 1, 2, 3, 2 ],
        [ 1, 1, 2, 2, 2 ],
        [ 3, 3, 2, 2, 2 ],
        [ 1, 3, 1, 1, 1 ],
        [ 1, 1, 3, 2, 2 ]
    );
    return @L;
}

sub BFS {
    my $L = shift();
    my $x = shift;
    my $y = shift;
    my $val = shift;
    my $visited = shift();

    my @A = ("$x,$y");
    push(@$visited, "$x,$y");
    my @queue = ("$x,$y");
    while (scalar(@queue) > 0) {
        my @next = ();
        my ($x, $y) = split(/,/, shift(@queue));
        for (my $i = $x - 1; $i < $x + 2; $i++) {
            for (my $j = $y - 1; $j < $y + 2; $j++) {
                if ($i >= 0 && $i <= $#$L && $j >= 0 && $j < scalar(@{$$L[0]})) {
                    my $ij = "$i,$j";
                    if ($$L[$i][$j] == $val && !grep (/^$ij$/, @$visited)) {
                        push(@A, $ij);
                        push(@$visited, $ij);
                        push(@next, $ij);
                    }
                }
            }
        }
        push(@queue, @next);
    }

    return @A;
}

my @L = generateList();
print(displayList(\@L));

my @visited = ();
my @B = ();

for (my $i = 0; $i <= $#L; $i++) {
    for (my $j = 0; $j < scalar(@{$L[$i]}); $j++) {
        my $ij = "$i,$j";
        if (!grep (/^$ij$/, @visited)) {
            my @A = BFS(\@L, $i, $j, $L[$i][$j], \@visited);
            push(@B, join(" | ", @A));
            @A = ();
        }
    }
}
$Data::Dumper::Indent = 1;
print Dumper \@B;

