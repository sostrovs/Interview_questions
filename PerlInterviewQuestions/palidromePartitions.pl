use strict;
use warnings;
use Data::Dumper;

sub isPalidrome {
    my $str = shift;
    my @L = split("", $str);
    for (my $i = 0; $i < ($#L + 1) / 2; $i++) {
        if ($L[$i] ne $L[$#L - $i]) {
            return 0;
        }
    }
    return 1;
}

sub getPalidromes {
    my $str = shift;
    my %D = ();
    my @L = split("", $str);
    for (my $i = 0; $i < length($str); $i++) {
        for (my $j = $i; $j < length($str); $j++) {
            my $sub_str = join("", @L[$i..$j]);
            if (isPalidrome($sub_str)) {
                if (exists($D{$i})) {
                    push(@{$D{$i}}, $sub_str);
                }
                else {
                    $D{$i}[0] = $sub_str;
                }
            }
        }
    }
    return %D;
}

sub getPartitions {
    my $D = shift;
    my $cur = shift;
    my $P = shift();
    my $L = shift();

    if ($cur >= keys %$D) {
        push(@$L, \@$P);
    } else {
        for(my $i = 0; $i < scalar @{$$D{$cur}}; $i++) {
            my @P_new = @$P;
            push(@P_new, $$D{$cur}[$i]);
            my $cur_new = $cur + length($P_new[-1]);
            getPartitions(\%$D, $cur_new, \@P_new, \@$L);
        }
    }
}

sub findPalidromePartitions {
    my $str = shift;
    my @L = ();
    my @P = ();
    my %D = getPalidromes($str);
    # print Dumper \%D;
    getPartitions(\%D, 0, \@P, \@L);
    return @L;
}

my $str = "aabaa";
print("$str\n");
my @L = findPalidromePartitions($str);
$Data::Dumper::Indent = 0;
print Dumper \@L;
