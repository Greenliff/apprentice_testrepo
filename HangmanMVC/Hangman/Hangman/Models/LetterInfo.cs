using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;

namespace Hangman.Models
{
    public class LetterInfo
    {
        [Key]
        public int LetterId { get; set; }

        [Required]
        public char Letter { get; set; }

        [Required]
        public int LanguageId { get; set; }

        public Language Language { get; set; }

        public ICollection<GuessedLetter> GuessedLetters { get; set; }
    }
}
