using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;

namespace Hangman.Models
{
    public class Language
    {
        [Key]
        public int LanguageId { get; set; }

        [Required]
        public string LanguageName { get; set; }

        public ICollection<LetterInfo> Letters { get; set; }

        public ICollection<WordInfo> Words { get; set; }

        public ICollection<Game> Games { get; set; }
    }
}
