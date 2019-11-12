use Irssi 20020101.0250 ();
$VERSION = "1.16";
%IRSSI = (
    authors     => 'Kathy Murdoch',
    contact     => 'my first name at nivan.net',
    name        => 'date',
    description => 'Adds the date as a statusbar item',
    license     => 'Public domain',
    url         => 'http://nivan.net/',
);

use Irssi::TextUI;

sub date ($$) {
	
	my ($sbitem, $get_size_only) = @_;
	

	($Sec,$Min,$Hour,$Day,$Month,$Year,$Week_Day) = (localtime); 
	$Year -= 100;
	$Month += 1;
	# Pad <10 with a 0
	if ($Day < 10) { $Day = "0".$Day; }
	if ($Month < 10) { $Month = "0".$Month; }
	if ($Year < 10) { $Year = "0".$Year; }

	my $format = sprintf("{sb %s/%s/%s}", $Day,$Month,$Year);
	$sbitem->default_handler($get_size_only, $format, undef, 1);
}


sub refreshdate {
	
	Irssi::statusbar_items_redraw("date");
}
	
Irssi::statusbar_item_register('date', undef, 'date');
Irssi::timeout_add(5000, "refreshdate", undef);

