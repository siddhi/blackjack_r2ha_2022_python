from .hand import Hand
from .deck import Deck
from .ansi import Ansi, Colour


class Game:
    def __init__(self):
        self.dealer_hand = Hand()
        self.player_hand = Hand()
        self.deck = Deck()

    @staticmethod
    def run():
        Game.display_welcome_screen()
        Game.wait_for_enter_from_user()

        Game.play_game()

        Game.reset_screen()

    @staticmethod
    def reset_screen():
        print(Ansi().reset())

    @staticmethod
    def play_game():
        game = Game()
        game.initial_deal()
        game.play()

    @staticmethod
    def wait_for_enter_from_user():
        print(Ansi().cursor(4, 1).fg(Colour.BLACK), end="")
        input("Hit [ENTER] to start...")

    @staticmethod
    def display_welcome_screen():
        print(Ansi().fg(Colour.WHITE).bg(Colour.WHITE).erase().cursor(1, 1), end="")
        print(str(Ansi().fg(Colour.BLACK)) + "Welcome to")
        print(str(Ansi().fg(Colour.RED)) + " JitterTed's")
        print(str(Ansi().fg(Colour.BLACK)) + " Blackjack game")

    def initial_deal(self):
        self.deal_round_of_cards()
        self.deal_round_of_cards()

    def play(self):
        self.player_turn()
        self.dealer_turn()
        self.display_final_game_state()
        self.determine_outcome()

    def deal_round_of_cards(self):
        # why: players first because this is the rule
        self.player_hand.draw_from(self.deck)
        self.dealer_hand.draw_from(self.deck)

    def determine_outcome(self):
        if self.player_hand.is_busted:
            print("You Busted, so you lose")
        elif self.dealer_hand.is_busted:
            print("Dealer went BUST, Player wins! Yay for you!!")
        elif self.player_hand.beats(self.dealer_hand):
            print("You beat the Dealer!")
        elif self.player_hand.pushes(self.dealer_hand):
            print("Push: Nobody wins, we'll call it even")
        else:
            print("You lost to the Dealer.")

    def dealer_turn(self):
        # Dealer makes its choice automatically based on a simple
        # heuristic (<=16 must hit, =>17 must stand)
        if not self.player_hand.is_busted:
            while self.dealer_hand.dealer_must_draw_card:
                self.dealer_hand.draw_from(self.deck)

    def player_turn(self):
        while not self.player_hand.is_busted:
            self.display_game_state()
            player_choice = self.input_from_player().lower()
            if player_choice.startswith("s"):
                break
            if player_choice.startswith("h"):
                self.player_hand.draw_from(self.deck)
                if self.player_hand.is_busted:
                    return
            else:
                print("You need to [H]it or [S]tand")

    def input_from_player(self):
        return input("[H]it or [S]tand? ")

    def display_game_state(self):
        print(Ansi().erase().cursor(1, 1), end="")
        print("Dealer has: ")
        print(self.dealer_hand.display_face_up_card())
        self.display_back_of_card()

        print()
        print("Player has: ")
        self.player_hand.display()
        print(f"({self.player_hand.value})")

    def display_back_of_card(self):
        print(Ansi().cursor_up(7).cursor_right(12), end="")
        print("┌─────────┐" + str(Ansi().cursor_down(1).cursor_left(11)), end="")
        print("│░░░░░░░░░│" + str(Ansi().cursor_down(1).cursor_left(11)), end="")
        print("│░ J I T ░│" + str(Ansi().cursor_down(1).cursor_left(11)), end="")
        print("│░ T E R ░│" + str(Ansi().cursor_down(1).cursor_left(11)), end="")
        print("│░ T E D ░│" + str(Ansi().cursor_down(1).cursor_left(11)), end="")
        print("│░░░░░░░░░│" + str(Ansi().cursor_down(1).cursor_left(11)), end="")
        print("└─────────┘" + str(Ansi().fg(Colour.BLACK)))

    def display_final_game_state(self):
        print(Ansi().erase().cursor(1, 1))
        print("Dealer has: ")
        self.dealer_hand.display()
        print(f"({self.dealer_hand.value})")

        print("Player has: ")
        self.player_hand.display()
        print(f"({self.player_hand.value})")
