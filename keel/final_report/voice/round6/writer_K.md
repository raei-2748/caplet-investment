# Writer K, voice round 6

## Warm-up: the IPS paragraph that starts "In January 2027 we'll use your first deposit"

Notes, a few words per sentence:
1. Jan 2027, first deposit, buys 10 Treasuries. Bonds or iBonds, whichever suits each year (in brackets). Each matures just before it's needed.
2. Held to the end = pay what they say. Dash. Prices moving: nothing to fear.
3. Today's yields, about $300k. Dash, "in other words": the whole first deposit.
4. Reassure, with an exclamation. Plan doesn't need yields to stay put.
5. Yields fall, ladder costs over $300k, "simply" finish it with the 2028 deposit.

Rebuilt from the notes alone:

In January 2027 we'll use your first deposit to buy 10 Treasuries (T-Bonds or iShares iBonds funds, whichever suits each year), each one maturing just before the payment it's there for. Held to the end, they pay what they say – so the price moving around in between is nothing for us to fear. At today's yields that comes to about $300,000, which is your whole first deposit. But don't worry – the plan doesn't rely on yields staying where they are! If they fall and the ladder ends up costing more than $300,000, we'll simply finish it with the 2028 deposit.

Where mine drifted: it explains a little more than it needs to ("the payment it's there for", "the price moving around in between") where the IPS trusts a short phrase ("just before it's needed", "no price fluctuations for us to fear"). I also lost "in other words" and the cheek of "worry not", which is a small piece of swagger, and exactly the bit that makes the original sound like them.

=== P1 ===
Before a single order went in, we wrote down what the finished book had to look like: an exact number of units for each of the 10 Treasury holdings, VT bought last with whatever cash was left, and never less than $1,000 in cash. So judging our implementation is simple – did we buy what we said we'd buy? Yes, though not without two scares.

The first, on 29-30 September, was two stale bond prices on WInS, about a percentage point of yield off the real Treasury curve. That matters more than it sounds. Too low a yield and we'd have been overpaying from day one; too high, and it probably meant a bond nobody was trading, which we might never get out of. So we made a rule: check every bond's yield against the Treasury curve before ordering, and buy only within 0.25 points. That band is about seven times the normal day-to-day scatter of Treasury prices around the curve, and wider than that scatter at its 2008 peak, so it lets a fair price through and stops a stale one cold.

The second was 7 October. The US market opened at 00:30 Sydney time (Eric fell asleep before it), and that day a click landed on the wrong row as the page scrolled. The order was gone, with no step to confirm it, and a market has no undo button. From then on, only Ray placed or cancelled orders.

All 11 orders filled on 7-8 October, Sydney time. All 10 Treasury holdings hit their targets exactly, every bond inside the band, cash never under $1,000, $200 in fees all up. VT ended at 167 units against 164 – the one holding off target, and the right one, since it was bought last from the cash left and no payment depends on it.

The catch is what the book couldn't show: WInS has one $300,000 account and no room for the 2028 deposit, so the book is Laura's whole plan "scaled to the model portfolio", $300,000 of its $450,000.

=== P2 ===
We set the test for our implementation before trading opened, so it was hard to fudge later. Each of the 10 Treasury holdings had a target number of units; VT came last, bought with whatever cash remained; and cash was never to dip below $1,000. Against that list, almost everything went to plan – but two things nearly didn't.

First, prices. On 29-30 September WInS showed two stale bond prices, roughly a percentage point of yield off the real Treasury curve – trouble either way round. A yield that's too low means paying too much; one that's too high probably means the bond isn't really trading, and we could be stuck with it. Our answer was a rule: every bond's yield gets checked against the curve before ordering, and anything more than 0.25 points out isn't bought. That's around seven times the normal day-to-day scatter of Treasury prices around the curve, and wider than that scatter even at its peak in 2008, so a fair price passes and a stale quote doesn't.

Then 7 October. Market open was 00:30 Sydney time – Eric fell asleep before it – and that day a click landed on the wrong row as the page scrolled; the order was gone with no step to confirm it. In a market a click is ink: once an order lands it's done, and there's no rubbing it out. From 7 October only Ray placed or cancelled orders.

All 11 orders filled over 7-8 October (Sydney time). Each of the 10 Treasury holdings landed exactly on target, every bond sat inside the band, cash never fell below its $1,000 floor, and fees came to $200. The one miss was VT, at 167 units instead of 164, and it's the right one to miss: bought last from the leftover cash, it's the only holding no payment depends on.

What the book couldn't show was the 2028 deposit. WInS has one $300,000 account, so the book is Laura's whole plan "scaled to the model portfolio": $300,000 of its $450,000.

=== P3 ===
The case asks for a dollar range Laura could give co-sponsors in 2031, and how confident she can be in it. On today's figures, the number that matters is the top: $115,000. That's her facility contribution – what she hands over, and the figure a co-sponsor counts when it plans around her. The range reaches down to $95,000, the part she has held since January 2028, when the late-2032 Treasury fund was bought. The rest of the top arrives with the 2031 move, when half her shares go into Treasuries before the meetings. So by the time Laura speaks, both ends are owned in Treasuries. The gap between them isn't us hedging our bets; it simply shows what she owned first and what the move added.

We worked each end out cautiously – almost stubbornly. Each assumes the cash waiting inside the funds earns no more interest, comes after the funds' 0.07% yearly fee, loses a further 0.5% for other fund costs, and is then rounded down to the nearest $5,000. The five funds of this kind that have already ended showed other costs of about 0.27%. The top is missed only if those costs pass roughly 3% of the funds' value, with cash earning nothing.

Which is why our answer on confidence isn't a percentage. Once both ends are owned, the range she states is certain – there's nothing left for markets to decide. After the move, the only thing still free to change is her flexibility, the half of the shares promised to no one (about $21,300 by January 2033, on our central figures). Never the range, and never a payment.

The timing does all the work. Before the move the top is still only an estimate: a 40% fall in world shares beforehand would leave it at about $95,000 to $105,000, with the bottom and every payment untouched. In our model, a top stated a year early would still not be owned in about 11 of 100 futures. So Laura states nothing until the move is done.

=== P4 ===
On today's figures Laura's range tops out at $115,000, and the top is the figure that counts. It's her facility contribution: the money she gives, and the number a co-sponsor books when it makes its own plans. Under it, the range runs down to $95,000 – the part she has held since January 2028, when the late-2032 Treasury fund (the floor) was bought. Everything between the two is what the 2031 move adds, when half her shares go into Treasuries ahead of the meetings. So the distance isn't a margin for error. By the time she names a figure, both ends are owned in Treasuries, and the range just records which part came first.

Both ends are pitched low on purpose. We assume cash sitting inside the funds earns no more interest; we take off the funds' 0.07% yearly fee and then a further 0.5% for their other costs; and we round down to the nearest $5,000. The five funds like these that have already reached their end ran other costs of about 0.27%, so the top would only be missed if those costs passed about 3% of the funds' value, with cash earning nothing.

Before the move, though, the top is still an estimate. A 40% fall in world shares beforehand would pull it to about $95,000-$105,000, while the bottom and every payment stayed where they were. Rub out the pencils while the ink is still tacky and it smears: name the top a year early, before the shares have moved, and in about 11 of 100 of our model futures it would not yet be owned. So Laura names it only once the move is done.

That's our answer on confidence, and why it isn't a percentage: once both ends are owned, the range she states is certain. What can still move after that is her flexibility – the half of the shares promised to no one, about $21,300 by January 2033 on our central figures – and nothing else, not the range and not a single payment.

=== NOTES ===
Writing from the IPS and the reflections, the plain passages came out closest to them where they conceded and turned ("That matters more than it sounds", "the right one to miss"), and furthest where I lined facts up in a list, as in the results paragraph, which reads more like a report than like the team talking. The click turn fitted almost for free, because the mis-click sentence already carries the plain fact (no step to confirm) and the turn only adds why that is final; the drying turn was harder, since it has to carry the 11-in-100 reason in the same sentence, and it nearly let the image become the reason for waiting, so I put the number straight after the colon. Neither turn cost understanding, but the P4 one is the line I'd most expect a reader to notice as a writer's move rather than the team's. I left out the four program officers because the facts here don't say whether they were real funders or a test panel, and the report should not describe a panel as real people unless they were.
