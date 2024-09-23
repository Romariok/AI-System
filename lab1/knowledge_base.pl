% Факты с одним аргументом
% Персонажи Dota 2
hero('Alchemist').
hero('Earth Spirit').
hero('Pudge').
hero('Arc Warden').
hero('Terrorblade').
hero('Bounty Hunter').
hero('Rubick').
hero('Tinker').
hero('Jakiro').
hero('Invoker').
hero('Void Spirit').
hero('Abaddon').

% Сложность
difficulty(1).
difficulty(2).
difficulty(3).

% Главный атрибут

attribute(strength).
attribute(agility).
attribute(intelligence).
attribute(universal).

% Роли

role(carry).
role(support).
role(nuker).
role(disabler).
role(durable).
role(escape).
role(pusher).
role(initiator).

% Тип персонажа

type(melee).
type(range).

% Факты с двумя аргументами
% Герой и его сложность

hero_difficulty('Alchemist', 1).
hero_difficulty('Earth Spirit', 3).
hero_difficulty('Pudge', 2).
hero_difficulty('Arc Warden', 3).
hero_difficulty('Terrorblade', 2).
hero_difficulty('Bounty Hunter', 1).
hero_difficulty('Jakiro', 1).
hero_difficulty('Tinker', 2).
hero_difficulty('Rubick', 3).
hero_difficulty('Abaddon', 1).
hero_difficulty('Void Spirit', 2).
hero_difficulty('Invoker', 3).

% Герой и его главный атрибут

hero_attribute('Alchemist', strength).
hero_attribute('Earth Spirit', strength).
hero_attribute('Pudge', strength).

hero_attribute('Arc Warden', agility).
hero_attribute('Terrorblade', agility).
hero_attribute('Bounty Hunter', agility).

hero_attribute('Tinker', intelligence).
hero_attribute('Rubick', intelligence).
hero_attribute('Jakiro', intelligence).

hero_attribute('Invoker', universal).
hero_attribute('Void Spirit', universal).
hero_attribute('Abaddon', universal).

% Герой и его роль

hero_role('Alchemist', carry).
hero_role('Alchemist', support).
hero_role('Alchemist', durable).
hero_role('Alchemist', disabler).
hero_role('Alchemist', initiator).
hero_role('Alchemist', nuker).

hero_role('Earth Spirit', nuker).
hero_role('Earth Spirit', escape).
hero_role('Earth Spirit', disabler).
hero_role('Earth Spirit', initiator).
hero_role('Earth Spirit', durable).

hero_role('Pudge', disabler).
hero_role('Pudge', initiator).
hero_role('Pudge', durable).
hero_role('Pudge', nuker).

hero_role('Arc Warden', carry).
hero_role('Arc Warden', escape).
hero_role('Arc Warden', nuker).

hero_role('Terrorblade', carry).
hero_role('Terrorblade', pusher).
hero_role('Terrorblade', nuker).

hero_role('Bounty Hunter', escape).
hero_role('Bounty Hunter', nuker).

hero_role('Rubick', support).
hero_role('Rubick', disabler).
hero_role('Rubick', nuker).

hero_role('Tinker', carry).
hero_role('Tinker', nuker).
hero_role('Tinker', pusher).

hero_role('Jakiro', support).
hero_role('Jakiro', nuker).
hero_role('Jakiro', pusher).
hero_role('Jakiro', disabler).

hero_role('Invoker', carry).
hero_role('Invoker', nuker).
hero_role('Invoker', disabler).
hero_role('Invoker', escape).
hero_role('Invoker', pusher).

hero_role('Void Spirit', carry).
hero_role('Void Spirit', escape).
hero_role('Void Spirit', nuker).
hero_role('Void Spirit', disabler).

hero_role('Abaddon', support).
hero_role('Abaddon', carry).
hero_role('Abaddon', durable).

% Герой и его тип

hero_type('Alchemist', melee).
hero_type('Earth Spirit', melee).
hero_type('Pudge', melee).
hero_type('Bounty Hunter', melee).
hero_type('Void Spirit', melee).
hero_type('Abaddon', melee).

hero_type('Rubick', range).
hero_type('Tinker', range).
hero_type('Jakiro', range).
hero_type('Invoker', range).
hero_type('Arc Warden', range).
hero_type('Terrorblade', range).

% Правила

