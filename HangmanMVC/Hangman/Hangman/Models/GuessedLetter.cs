using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;

namespace Hangman.Models
{
    public class GuessedLetter
    {
        [Key]
        public int GuessedLetterId { get; set; }

        [Required]
        public int LetterId { get; set; }

        public LetterInfo Letters { get; set; }

        [Required]
        public int WordInGameId { get; set; }

        public WordInGame WordsInGames { get; set; }
    }
}
