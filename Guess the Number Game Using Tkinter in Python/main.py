"""
MASA Cipher Mind - Number Decryption Game
Developer: MASA
"""

import random
import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class MasaCipherGame(ctk.CTk):
    LEVELS = {
        "Novice": (1, 50, 8),
        "Operative": (1, 100, 7),
        "CyberMaster": (1, 500, 10),
    }

    def __init__(self):
        super().__init__()

        self.title("MASA Cipher Mind")
        self.geometry("460x580")
        self.resizable(False, False)
        self.configure(fg_color="#0D111A")

        self.current_level = "Operative"
        self.target_val = 0
        self.max_attempts = 7
        self.remaining_attempts = 7
        self.score_streak = 0

        self._build_ui()
        self._init_round()

    def _build_ui(self):
        header_card = ctk.CTkFrame(self, fg_color="#151C2C", corner_radius=14)
        header_card.pack(fill="x", padx=20, pady=(20, 12))

        title = ctk.CTkLabel(
            header_card,
            text="MASA CIPHER MIND",
            font=ctk.CTkFont(family="Segoe UI", size=18, weight="bold"),
            text_color="#F43F5E",
        )
        title.pack(pady=(12, 2))

        subtitle = ctk.CTkLabel(
            header_card,
            text="Tactical Numeric Decryption Protocol",
            font=ctk.CTkFont(size=11),
            text_color="#94A3B8",
        )
        subtitle.pack(pady=(0, 12))

        diff_row = ctk.CTkFrame(self, fg_color="#151C2C", corner_radius=12)
        diff_row.pack(fill="x", padx=20, pady=5)

        lbl_diff = ctk.CTkLabel(diff_row, text="PROTOCOL LEVEL", font=ctk.CTkFont(size=11, weight="bold"), text_color="#94A3B8")
        lbl_diff.pack(side="left", padx=16, pady=8)

        self.level_selector = ctk.CTkSegmentedButton(
            diff_row,
            values=list(self.LEVELS.keys()),
            command=self._on_level_change,
            selected_color="#E11D48",
            selected_hover_color="#BE123C",
        )
        self.level_selector.set("Operative")
        self.level_selector.pack(side="right", padx=14, pady=8)

        self.card_main = ctk.CTkFrame(self, fg_color="#151C2C", corner_radius=16)
        self.card_main.pack(fill="both", expand=True, padx=20, pady=10)

        self.info_badge = ctk.CTkLabel(
            self.card_main,
            text="Range: 1 - 100",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color="#38BDF8",
            fg_color="#0F2137",
            corner_radius=8,
            padx=12,
            pady=4,
        )
        self.info_badge.pack(pady=(15, 6))

        self.attempts_lbl = ctk.CTkLabel(
            self.card_main,
            text="Attempts Remaining: 7",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color="#FBBF24",
        )
        self.attempts_lbl.pack(pady=(0, 6))

        self.feedback_lbl = ctk.CTkLabel(
            self.card_main,
            text="Initialize decryption by submitting a value",
            font=ctk.CTkFont(size=13),
            text_color="#E2E8F0",
            wraplength=380,
        )
        self.feedback_lbl.pack(pady=8)

        self.proximity_bar = ctk.CTkProgressBar(
            self.card_main,
            width=360,
            height=10,
            corner_radius=5,
            progress_color="#F43F5E",
        )
        self.proximity_bar.pack(pady=10)
        self.proximity_bar.set(0)

        entry_row = ctk.CTkFrame(self.card_main, fg_color="transparent")
        entry_row.pack(fill="x", padx=20, pady=10)

        self.entry_guess = ctk.CTkEntry(
            entry_row,
            placeholder_text="Enter cipher guess...",
            font=ctk.CTkFont(family="Consolas", size=16),
            height=42,
            justify="center",
            corner_radius=10,
        )
        self.entry_guess.pack(side="left", fill="x", expand=True, padx=(0, 8))
        self.entry_guess.bind("<Return>", lambda _: self._submit_guess())

        self.action_btn = ctk.CTkButton(
            entry_row,
            text="Verify",
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color="#E11D48",
            hover_color="#BE123C",
            width=80,
            height=42,
            corner_radius=10,
            command=self._submit_guess,
        )
        self.action_btn.pack(side="right")

        self.streak_lbl = ctk.CTkLabel(
            self.card_main,
            text="Consecutive Decryptions: 0",
            font=ctk.CTkFont(size=11),
            text_color="#64748B",
        )
        self.streak_lbl.pack(side="bottom", pady=10)

    def _on_level_change(self, level):
        self.current_level = level
        self._init_round()

    def _init_round(self):
        low, high, attempts = self.LEVELS[self.current_level]
        self.target_val = random.randint(low, high)
        self.max_attempts = attempts
        self.remaining_attempts = attempts

        self.info_badge.configure(text=f"Target Range: {low} - {high}")
        self.attempts_lbl.configure(text=f"Attempts Remaining: {self.remaining_attempts}", text_color="#FBBF24")
        self.feedback_lbl.configure(text="System ready. Submit your numeric estimate.", text_color="#E2E8F0")
        self.proximity_bar.set(0)
        self.entry_guess.delete(0, "end")
        self.entry_guess.configure(state="normal")
        self.action_btn.configure(text="Verify", command=self._submit_guess)

    def _submit_guess(self):
        raw = self.entry_guess.get().strip()
        low, high, _ = self.LEVELS[self.current_level]

        try:
            val = int(raw)
            if not (low <= val <= high):
                self.feedback_lbl.configure(text=f"Value out of bounds ({low} - {high})", text_color="#FB923C")
                return
        except ValueError:
            self.feedback_lbl.configure(text="Invalid cipher format. Integers only.", text_color="#FB923C")
            return

        self.remaining_attempts -= 1
        self.attempts_lbl.configure(text=f"Attempts Remaining: {self.remaining_attempts}")

        total_range = high - low
        diff = abs(self.target_val - val)
        closeness = max(0.0, 1.0 - (diff / float(total_range)))
        self.proximity_bar.set(closeness)

        if val == self.target_val:
            self.score_streak += 1
            self.streak_lbl.configure(text=f"Consecutive Decryptions: {self.score_streak}")
            self.feedback_lbl.configure(
                text=f"DECRYPTION SUCCESS! Code {self.target_val} cracked!",
                text_color="#34D399",
            )
            self.entry_guess.configure(state="disabled")
            self.action_btn.configure(text="Next Round", command=self._init_round)
        elif self.remaining_attempts <= 0:
            self.score_streak = 0
            self.streak_lbl.configure(text="Consecutive Decryptions: 0")
            self.feedback_lbl.configure(
                text=f"SECURITY LOCKOUT! Cipher was: {self.target_val}",
                text_color="#F43F5E",
            )
            self.entry_guess.configure(state="disabled")
            self.action_btn.configure(text="Restart", command=self._init_round)
        else:
            hint = "Higher 📈" if val < self.target_val else "Lower 📉"
            self.feedback_lbl.configure(
                text=f"Target is {hint} | Proximity: {int(closeness * 100)}%",
                text_color="#38BDF8",
            )
            self.entry_guess.delete(0, "end")


if __name__ == "__main__":
    app = MasaCipherGame()
    app.mainloop()
