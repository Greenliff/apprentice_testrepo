using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;

namespace Hangman.Models
{
    public class WordApproval
    {
        [Key]
        public int WordApprovalId { get; set; }

        [Required]
        public DateTime Date { get; set; }

        [Required]
        public int WordId { get; set; }

        public WordInfo Word { get; set; }

        [Required]
        public int UserId { get; set; }

        public User User { get; set; }
    }
}
