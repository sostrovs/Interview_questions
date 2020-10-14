use strict;
use warnings;
use Data::Dumper;

sub getPrimeNums {
    die "Wrong number of args" if (scalar(@_) != 1);
    my $n = $_[0];
    my @tf = map "True", (1 .. $n + 1);
    my @primes = ();
    for (my $i = 2; $i <= $#tf; $i++) {
        if ($tf[$i] eq "True") {
            push(@primes, $i);
            for (my $j = $i + $i; $j <= $#tf; $j += $i) {
                $tf[$j] = "False";
            }
        }
    }
    return @primes;
}

my @primes = getPrimeNums(97);
$Data::Dumper::Indent = 0;
print Dumper \@primes;
