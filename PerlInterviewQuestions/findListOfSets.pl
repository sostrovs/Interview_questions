use strict;
use warnings;
use Data::Dumper;

sub getDictionary {
    my $L = shift();
    my %D = ();
    for (my $i = 0; $i < $#$L; $i++) {
        for (my $j = 0; $j < scalar(@{$$L[$i]}); $j++) {
            my $A = $$L[$i + 1];
            $D{$$L[$i][$j]} = ();
            for my $el (@$A) {
                push(@{$D{$$L[$i][$j]}}, $el);
            }
        }
    }
    return %D;
}

sub getSets {
    my $D = shift;
    my $cur = shift;
    my $A = shift();
    my $P = shift();

    if(!exists($$D{$cur})) {
        push(@$A, $cur);
        push(@$P, \@$A);
    } else {
        push(@$A, $cur);
        for(my $i = 0; $i < scalar(@{$$D{$cur}}); $i++) {
            my @A_copy =  @{$A};
            getSets(\%$D, $$D{$cur}[$i], \@A_copy, \@$P);
        }
    }
}

sub findAllSets {
    my $D = shift;
    my $L = shift();
    my @P = ();

    for (my $i = 0; $i < scalar(@{$$L[0]}); $i++) {
        my @A = ();
        getSets(\%$D, $$L[0][$i], \@A, \@P)
    }

    return @P;
}

my @L = (
    [ '1', '2', '3' ],
    [ 'a', 'b', 'c' ],
    [ 'Alpha', 'Beta' ]
);
$Data::Dumper::Indent = 0;
print Dumper \@L;
print("\n");
my %D = getDictionary(\@L);
print("\n");
$Data::Dumper::Indent = 0;
print Dumper %D;
print("\n\n");

my @P = findAllSets(\%D, \@L);
$Data::Dumper::Indent = 0;
print Dumper \@P;

print("\n$#P");


