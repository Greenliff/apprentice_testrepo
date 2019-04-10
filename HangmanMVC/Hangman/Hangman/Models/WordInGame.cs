using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;

namespace Hangman.Models
{
    public class WordInGame
    {
        [Key]
        public int WordInGameId { get; set; }

        [Required]
        public WordState State { get; set; }

        [Required]
        public int WordId { get; set; }

        public WordInfo Word { get; set; }

        [Required]
        public int GameId { get; set; }

        public Game Game { get; set; }

        public ICollection<GuessedLetter> GuessedLetters { get; set; }
    }

    public enum WordState
    {
        Correct,
        Wrong,
        Current
    }
}
